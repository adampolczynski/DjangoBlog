from django.db import models
from blog.models import Entry
from articles.models import Article
from django.contrib.auth.models import User
from BlogProj.tasks import count_comments_for_entry, count_comments_for_article # importing celery tasks

# Create your models here.

class Comment(models.Model): 

	body = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)
	entry = models.ForeignKey(
		Entry,on_delete=models.CASCADE, null=True, related_name="comments")
	article = models.ForeignKey(
		Article, on_delete=models.CASCADE, null=True, related_name="comments")
	user = models.CharField(max_length=20, default='guest') # only username fo relation is not needed

	def save(self, *args, **kwargs):
		if (self.entry is None): # if we actually submit comment for article
			count_comments_for_article.delay(self.article.id)
		else:
			count_comments_for_entry.delay(self.entry.id)
		super(Comment, self).save(*args, **kwargs)

	def __str__(self):
		return '%s ...' % self.body[:10]

	def __unicode__(self):
		return '%s ...' % self.body[:10]