from django.urls import *
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dictionary/', include('dictionary.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]
