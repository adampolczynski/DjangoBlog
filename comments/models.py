from django.db import models
from blog.models import Entry
from articles.models import Article
from BlogProj.tasks import count_comments_for_entry # importing celery task

# Create your models here.
DEFAULT_ID = -1 # as a default value for foreign keys, id -1 does not exist

class Comment(models.Model): 

	body = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)
	entry = models.ForeignKey(
		Entry,on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True, related_name="comments")
	article = models.ForeignKey(
		Article, on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True, related_name="comments")

	def save(self, *args, **kwargs):
		count_comments_for_entry.delay(self.entry.id)
		super(Comment, self).save(*args, **kwargs)

	def __str__(self):
		return '%s ...' % self.body[:10]

	def __unicode__(self):
		return '%s ...' % self.body[:10]