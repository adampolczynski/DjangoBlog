from django.db import models
import blog
import articles
# Create your models here.

class Comment(models.Model):
	body = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)

	# every comment is related with entry or article
	entry = models.ForeignKey(						
        blog.models.Entry, related_name='comments', default=0)
	article = models.ForeignKey(
        articles.models.Article, related_name='comments', default=0)