from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from mainsite import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stephens.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.home,name='site_home'),
)
