from django.db import models
from django.template.defaultfilters import slugify
from datetime import date
# Create your models here.
class PastArticle(models.Manager): # manager that filters objects by time less than today
	def get_queryset(self):
		today = date.today()
		return super(PastArticle, self).get_queryset().filter(published__gt=today)
class Article(models.Model): # differs from blog entry
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	published = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	comments_count = models.IntegerField(default=0)

	objects = models.Manager()
	past_objects = PastArticle()

	def get_absolute_url(self): # get url to single entry
		return "/article/%s/" % self.slug

	def save(self, *args, **kwargs):
	        self.slug = slugify(self.title)
	        super(Article, self).save(*args, **kwargs)

	def __str__(self):# when called display title, not entry object
		return self.title

	def __unicode__(self):
		return '%s' % self.title