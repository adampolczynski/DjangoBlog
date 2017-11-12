from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from .models import Entry

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