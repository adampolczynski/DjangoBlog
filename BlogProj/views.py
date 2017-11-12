from django import views
from django.http import HttpResponse
from haystack.query import SearchQuerySet
import json
#     only one view here in root app, autocomplete for haystack

def autocomplete(request): # for haystack
	sqs = SearchQuerySet().autocomplete(body=request.GET.get('q','')[:10])
	suggestions = [result.title[:30].strip("[]") for result in sqs]
	# Make sure you return a JSON object, not a bare list.
	# Otherwise, you could be vulnerable to an XSS attack.
	the_data = json.dumps({'results': suggestions})
	return HttpResponse(the_data, content_type='application/json')

	def get_queryset(self):
		queryset = super(self).get_queryset()