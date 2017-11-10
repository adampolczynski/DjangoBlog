# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
from blog.models import Entry
from articles.models import Article

from django.core.mail import send_mail

@task # amazing those tasks :D
def count_comments_for_entry(id):
	model = Entry.objects.get(pk=id)
	model.comments_count=model.comments_count+1
	model.save()
	return 'adding 1 to entry comments_count'

@task
def count_comments_for_article(id):
	model = Article.objects.get(pk=id)
	model.comments_count=model.comments_count+1
	model.save()
	return 'adding 1 to article comments_count'
	
@task
def send_confirmation_email(text,email):
	send_mail(
		'DjangoBlog shopping',
		text,
		'androdappshelper@gmail.com',
		[email],
		fail_silently=False,
		)
	return 'send confirmation should be sent bejbe'