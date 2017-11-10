from django.contrib import admin
from .models import Entry
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	exclude = ['posted','comments_count','slug',]
	#prepopulated_fields = {'slug': ('title',)} # not necessary while were excluding slug
	readonly_fields = ('pub_date','modified',)
	# def get_readonly_fields(self, request, obj=None): # not working with prepopulated_fields, have to do instruction
	# 	if obj: #In edit mode
	# 		return ('slug',)
	# 	return self.readonly_fields

admin.site.register(Entry, EntryAdmin)