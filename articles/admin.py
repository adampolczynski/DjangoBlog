from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	exclude = ['posted','comments_count','slug',]
	readonly_fields = ('pub_date','modified',)

admin.site.register(Article, ArticleAdmin)
