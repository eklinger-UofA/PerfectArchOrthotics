from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'views.index', name='index'),
                       url(r'^login/', 'views.user_login', name='user_login'),
                       url(r'^logout/', 'views.user_logout', name='user_logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^clients/', include('clients.urls')),
                       url(r'^inventory/', include('inventory.urls')),
                       )
