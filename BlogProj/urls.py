from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

# importing views
from blog import views as blogentry
from articles import views as blogarticle
from products import views as productsview
from comments.views import CommentView

if settings.DEBUG:			# because of jdtd template rendering error while DEBUG true
	import debug_toolbar

urlpatterns = [ # need to clean those urls, it is messy
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls',)),
    url(r'^allauth/', include('allauth.urls',)), #django registration
    url(r'^search/', include('haystack.urls')),
    url(r'^entries/', blogentry.index),
    url(r'^$', blogentry.index), # default go to entries, causing loginas problem
    url(r'^articles/', blogarticle.index),
    url(r'^products/', productsview.index),
	url(r'^entry/(?P<slug>[^\.]+)/',  # for single entry
    	blogentry.view_post, 
    	name='view_entry'),
    url(r'^article/(?P<slug>[^\.]+)/', # for single article 
    	blogarticle.view_post, 
    	name='view_article'),

    url(r'^add_comment/$', CommentView.as_view()),

    url(r'^__debug__/', include(debug_toolbar.urls)), # look up, below imports
]

#urlpatterns += url(r'^hijack/', include('hijack.urls')), # for logging as other user
urlpatterns += url(r'^admin/', include('loginas.urls')),
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
urlpatterns += url(r'^', blogentry.index), #NOTE: without $
