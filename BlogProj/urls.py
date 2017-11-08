from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blogviews

if settings.DEBUG:			# because of jdtd template rendering error while DEBUG true
	import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blogviews.index),
	url(r'^post/(?P<slug>[^\.]+)/', 
    	blogviews.view_post, 
    	name='view_entry'),
    
    url(r'^__debug__/', include(debug_toolbar.urls)), # look up, below imports
]
