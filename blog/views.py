from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Entry
from django.template.loader import get_template


def index(request):
	# template = get_template('entry_list.html') # actual way for template rendering, apply this
	# html = template.render({'posts': Entry.past_objects.all()[:5], 'type':'entry'})
    return render_to_response('entry_list.html', {
        'posts': Entry.past_objects.all()[:5],
        'type': 'entry'
    }, context_instance=RequestContext(request)) # because of csfr token, have to update because deprecated

def view_post(request, slug):   
    return render_to_response('entry.html', {
        'post': get_object_or_404(Entry, slug=slug),
        'type': 'entry'
    }, context_instance=RequestContext(request)) # upgrade this

def entries(request): # haystack view for custom form
    form = EntriesSearchForm(request.GET)
    entrys = form.search()
    return render_to_response('search_result.html', {'entrys': entrys})