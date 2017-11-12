from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.views.generic.edit import FormView # this time class based view 
from blog.models import Entry
from articles.models import Article

from django.core.urlresolvers import reverse_lazy
# Create your views here.

class CommentView(FormView):
	template_name = 'comment_result.html' # in case of error going to main page
	success_url = '/' # overriding this by form_valid return
	form_class = CommentForm

	def form_invalid(self, form): # we can throw some custom feedback
		return super(CommentView, self).form_invalid(form)

	def form_valid(self, form):
		our_id = form.cleaned_data['id']
		our_type = form.cleaned_data['type']
		our_body = form.cleaned_data['body']
		our_user = form.cleaned_data['user']

		if (our_type=='entry'): # if it is entry were referencing entry
			entry = Entry.objects.only('id').get(id=our_id)
			comment = Comment(body=our_body, user=our_user, entry=entry)
		else: # else we refer to article
			article = Article.objects.only('id').get(id=our_id)
			comment = Comment(body=our_body, user=our_user, article=article)

		comment.save()
		# return render(self.request, 'comment_result.html', {
		# 	'valid':True
		# 	})
		return super(CommentView, self).form_valid(form)