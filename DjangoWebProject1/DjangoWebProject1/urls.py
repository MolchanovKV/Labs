"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from HWn import views


urlpatterns = patterns('',
    
    url(r'^$', views.home),
    url(r'^usename/$', views.username),
    
)
