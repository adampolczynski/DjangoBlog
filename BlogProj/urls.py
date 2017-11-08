from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blogviews
from articles import views as blogarticle
from comments.views import CommentView
if settings.DEBUG:			# because of jdtd template rendering error while DEBUG true
	import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entries/', blogviews.index),
    url(r'^articles/', blogarticle.index),
    url(r'^', blogviews.index),
	url(r'^entry/(?P<slug>[^\.]+)/',  # for single entry
    	blogviews.view_post, 
    	name='view_entry'),
    url(r'^article/(?P<slug>[^\.]+)/', # for single article 
    	blogviews.view_post, 
    	name='view_article'),

    url(r'^add_comment/$', CommentView.as_view()),

    url(r'^__debug__/', include(debug_toolbar.urls)), # look up, below imports
]
