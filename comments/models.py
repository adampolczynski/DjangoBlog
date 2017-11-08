from django.db import models
import blog
import articles
# Create your models here.
DEFAULT_ID = -1 # as a default value for foreign keys, id -1 does not exist

class Comment(models.Model): 
	body = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)

	# every comment have to be related with entry or article
	entry = models.ForeignKey(
		blog.models.Entry,on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True)
	article = models.ForeignKey(
		articles.models.Article, on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True)

	def __str__(self):# when called display title, not entry object
		return '%s ...' % self.body[:10]

	def __unicode__(self):
		return '%s ...' % self.body[:10]