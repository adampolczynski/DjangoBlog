from django.db import models
import blog
import articles
# Create your models here.
DEFAULT_ID = 1 # as a default value for foreign keys

class Comment(models.Model): 
	body = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)

	# every comment have to be related with entry or article
	entry = models.ForeignKey(
		blog.models.Entry, to_field='title',on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True)
	article = models.ForeignKey(
		articles.models.Article, to_field='title', on_delete=models.CASCADE, 
		default=DEFAULT_ID, blank=True, null=True)