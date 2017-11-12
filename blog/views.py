from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from .models import Entry
from haystack.query import SearchQuerySet
import json

def index(request):
	return render_to_response('entry_list.html', {
        'posts': Entry.past_objects.all()[:5],
        'type': 'entry'
    }, context_instance=RequestContext(request)) 

def single_post(request, slug):   
    return render_to_response('entry.html', {
        'post': get_object_or_404(Entry, slug=slug),
        'type': 'entry'
    }, context_instance=RequestContext(request)) 

def autocomplete(request): # for haystack
	print('autocomplete---------------')
	sqs = SearchQuerySet().autocomplete(body=request.GET.get('q', ''))[:5]
	suggestions = [result.body[:30].strip("[]") for result in sqs]
	# Make sure you return a JSON object, not a bare list.
	# Otherwise, you could be vulnerable to an XSS attack.
	the_data = json.dumps({'results': suggestions})
	return HttpResponse(the_data, content_type='application/json')

	def get_queryset(self):
		queryset = super(self).get_queryset()