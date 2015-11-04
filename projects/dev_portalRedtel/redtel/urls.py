#redtel URL Configuration

from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
						(r'^admin/', include(admin.site.urls) ),
                       url(r'^$', 'portal.views.index', name='index'),
                       url(r'^ingresar$', login, {'template_name': 'login.html', }, name="login"),
                       url(r'^home$', 'portal.views.home', name='home'),
                       url(r'^home/mis_datos$', 'portal.views.mis_datos', name='mis_datos'),
                       url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
                       url(r'^administrador$', 'portal.views.administrador', name="administrador"),
                       url(r'^administrador/cargar_usuarios$', 'portal.views.cargar_usuarios', name="cargar_usuarios"),
)

