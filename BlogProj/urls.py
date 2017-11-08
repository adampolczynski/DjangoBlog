from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

# importing views
from blog import views as blogentry
from articles import views as blogarticle
from comments.views import CommentView

if settings.DEBUG:			# because of jdtd template rendering error while DEBUG true
	import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls',)),
    url(r'^allauth/', include('allauth.urls',)), #django registration

    url(r'^entries/', blogentry.index),
    url(r'^articles/', blogarticle.index),
	url(r'^entry/(?P<slug>[^\.]+)/',  # for single entry
    	blogentry.view_post, 
    	name='view_entry'),
    url(r'^article/(?P<slug>[^\.]+)/', # for single article 
    	blogarticle.view_post, 
    	name='view_article'),

    url(r'^add_comment/$', CommentView.as_view()),

    url(r'^', blogentry.index), # if nothing matches then go to entries index
    url(r'^__debug__/', include(debug_toolbar.urls)), # look up, below imports
]
