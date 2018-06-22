from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^login/', 'loginsys.views.login', name='login'),
    url(r'^logout/', 'loginsys.views.logout', name='logout'),
    #url(r'^register/', 'loginsys.views.register', name='register'),

    url(r'^signup/', 'loginsys.views.signup', name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 'loginsys.views.activate', name='activate'),
]
