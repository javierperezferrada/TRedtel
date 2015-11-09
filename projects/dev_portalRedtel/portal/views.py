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
from .models import Liquidacion
from .models import Palabra
from .models import Document
from django.contrib import messages
import csv
from .forms import UploadFileForm


def index(request):
    return render_to_response('index.html')

@login_required()
def home(request):
   return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))

@login_required()
def mis_datos(request):
	usuario = get_object_or_404(Usuario, nombre=request.user.username)
	return render_to_response('mis_datos.html', {'usuario': usuario}, context_instance=RequestContext(request))

@login_required()
def mis_liquidaciones(request):
	usuario = get_object_or_404(Usuario, nombre=request.user.username)
	liquidacion = get_object_or_404(Liquidacion, rut_trabajador=usuario.rut)
	return render_to_response('mis_liquidaciones.html', {'usuario': usuario}, context_instance=RequestContext(request))

@permission_required('portal.puede_cargar', login_url="/ingresar") 
def cargar_usuarios(request):	
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            reader = csv.reader(request.FILES['docfile'])
            for row in reader:
                palabras = Palabra()
                palabras.id = row[0]
                palabras.tipo = row[1]
                palabras.palabra1 = row[2]
                palabras.palabra2 = row[3]
                palabras.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render_to_response('cargar_usuarios.html', {'form': form}, context_instance=RequestContext(request))

@permission_required('portal.puede_cargar', login_url="/ingresar")  
def cargar_liquidaciones(request):
	return render_to_response('cargar_liquidaciones.html', context_instance=RequestContext(request))

def load_info(request):
	reader = csv.reader(open("info.csv"))
	for row in reader:
		palabras = Palabra()
		palabras.id = row[0]
		palabras.tipo = row[1]
		palabras.palabra1 = row[2]
		palabras.palabra2 = row[3]
		palabras.save()
	return HttpResponseRedirect('/')

