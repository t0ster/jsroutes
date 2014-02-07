# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns("jsroutes.views",
    url(r"^routes\.js$", "routes", name="jsroutes"),
)
