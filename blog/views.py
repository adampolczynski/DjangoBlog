from .models import Entry
import articles
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'posts': Entry.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_entry.html', {
        'post': get_object_or_404(Entry, slug=slug)
    })
