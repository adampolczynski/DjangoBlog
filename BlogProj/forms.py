from django import forms
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
class MySearchForm(SearchForm):
	def __init__(self, *args, **kwargs):
		super(MySearchForm, self).__init__(*args, **kwargs)
		self.fields['q'].widget.attrs.update({'class' : 'form-control'})
	
	#entry = forms.CharField(max_length=30)
	q = forms.CharField(required=False, label=('Search'))
	def search(self):
		if not self.is_valid():
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
			return self.no_query_found()

		sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

		if self.load_all:
			sqs = sqs.load_all()

		return sqs