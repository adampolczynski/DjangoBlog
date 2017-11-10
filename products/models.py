from django.db import models

# Create your models here.

class Product(models.Model):

	name = models.CharField(max_length=20)
	picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/no-img.jpg')
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return '%s' % self.name

	def __unicode__(self):
		return '%s' % self.name