from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required,permission_required
from .models import Usuario


def index(request):
    return render_to_response('index.html')

@login_required()
def home(request):
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))

@login_required()
def mis_datos(request):
	usuario = get_object_or_404(Usuario, pk=1)
	return render_to_response('mis_datos.html', {'usuario': usuario}, context_instance=RequestContext(request))

@permission_required('portal.puede_cargar', login_url="/ingresar") 
def administrador(request):
	return render_to_response('admin.html', context_instance=RequestContext(request))



@permission_required('portal.puede_cargar', login_url="/ingresar")  
def cargar_usuarios(request):
	return render_to_response('c_usuarios.html', context_instance=RequestContext(request))