from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	exclude = ['posted','comments_count','slug',]
	readonly_fields = ('published','modified',)

admin.site.register(Article, ArticleAdmin)
