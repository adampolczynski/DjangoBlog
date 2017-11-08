from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Article

# Create your views here.

def index(request):
    return render_to_response('entry_list.html', {
        'posts': Article.past_objects.all()[:5],
        'type': 'article'
    }, context_instance=RequestContext(request)) # because of csfr token, have to update because deprecated

def view_post(request, slug):   
    return render_to_response('entry.html', {
        'post': get_object_or_404(Article, slug=slug),
        'type': 'article'
    })
