from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	published = models.DateTimeField(auto_now=True)
	comments_count = models.IntegerField(default=0) # this has to be done with celery

	def get_absolute_url(self):
		return "/post/%s/" % self.slug

	def save(self, *args, **kwargs):
	        self.slug = slugify(self.title)
	        super(Entry, self).save(*args, **kwargs)

	def __str__(self):# when called display title, not entry object
		return self.title

	def __unicode__(self):
		return '%s' % self.title