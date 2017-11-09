from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.views.generic.edit import FormView # this time class based view maybe
from blog.models import Entry
from articles.models import Article
# Create your views here.

class CommentView(FormView):
	template_name = 'comment_error.html' # have to go to single entry or article view
	success_url = '/' # back to index after success submit
	form_class = CommentForm
	def form_valid(self, form):
		our_id = form.cleaned_data['id']
		our_type = form.cleaned_data['type']

		if (our_type=='entry'): # if it is entry were referencing entry
			entry = Entry.objects.only('id').get(id=our_id)
			comment = Comment(
			body=form.cleaned_data['body'],
			entry=entry)
		else: # else we refer to article
			article = Article.objects.only('id').get(id=our_id)
			comment = Comment(
			body=form.cleaned_data['body'],
			article=article)

		comment.save()

		return super(CommentView, self).form_valid(form)