#redtel URL Configuration

from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
                       url(r'^$', 'portal.views.index', name='index'),
                       url(r'^ingresar$', login, {'template_name': 'login.html', }, name="login"),
                       url(r'^home$', 'portal.views.home', name='home'),
                       url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
                       url(r'^admin$', 'portal.views.administrador', name="administrador"),
                       url(r'^admin/cargar_usuarios$', 'portal.views.cargar_usuarios', name="cargar_usuarios"),
)

