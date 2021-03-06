from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls', namespace="docs")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("jsroutes.urls"))
)
