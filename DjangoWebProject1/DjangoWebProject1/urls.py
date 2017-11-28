"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm


urlpatterns = patterns('',
    
    url(r'^$', 'DjangoWebProject1.HWn.views.home', name='home'),
    
)
