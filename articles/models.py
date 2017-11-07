from django.db import models

# Create your models here.

class Article(models.Model): # differs from blog entry
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	published = models.DateTimeField(auto_now=True)
	comments_count = models.IntegerField()

	def __unicode__(self):
		return '%s' % self.title

		@permalink
		def get_absolute_url(self):
			return ('blog_post', None, { 'slug': self.slug })