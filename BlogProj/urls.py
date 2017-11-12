from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.static import serve
# importing views
from blog import views as blogentry
from articles import views as blogarticle
from products import views as products
from comments.views import CommentView

urlpatterns = [ # need to clean those urls, it is messy
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls',)),
    url(r'^allauth/', include('allauth.urls',)), #django registration
    # search stuff
    url(r'^search/', include('haystack.urls')),
    url(r'^search/autocomplete/', blogentry.autocomplete),
    # 
    url(r'^articles/', blogarticle.index),
    url(r'^products/', products.index),
	url(r'^entry/(?P<slug>[^\.]+)/',  # for single entry
    	blogentry.single_post, 
    	name='single_entry'),
    url(r'^article/(?P<slug>[^\.]+)/', # for single article 
    	blogarticle.single_post, 
    	name='single_article'),

    url(r'^add_comment/$', CommentView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += url(r'^admin/', include('loginas.urls')),
urlpatterns += url(r'^media/(?P<path>.*)$', serve),
urlpatterns += url(r'^', blogentry.index), # MAIN PAGE - entries

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += url(r'^__debug__/', include(debug_toolbar.urls)), # look up, below imports