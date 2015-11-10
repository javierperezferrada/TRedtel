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
	usuario = get_object_or_404(Usuario, id=request.user.id)
	return render_to_response('mis_datos.html', {'usuario': usuario}, context_instance=RequestContext(request))

@login_required()
def obtener_certificado(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    return render_to_response('obtener_certificado.html', {'usuario': usuario}, context_instance=RequestContext(request))

@login_required()
def mis_liquidaciones(request):
	usuario = get_object_or_404(Usuario, id=request.user.id)
	liquidacion = get_object_or_404(Liquidacion, Usuario_rut=usuario.rut)
	return render_to_response('mis_liquidaciones.html', {'liquidacion': liquidacion}, context_instance=RequestContext(request))

@login_required()
def copias_liquidaciones(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    return render_to_response('copias_liquidaciones.html', {'usuario': usuario}, context_instance=RequestContext(request))

@permission_required('portal.puede_cargar', login_url="/ingresar") 
def cargar_usuarios(request):	
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(request.FILES['docfile'])
            for row in reader:
                if row[0]=='id':
                    print 'cabecera'
                else:
                    user = User.objects.create_user(id=row[0],
                        username=row[1],first_name = row[2],
                        last_name=row[3],email=row[4],password=row[5]) 
                    usuarios = Usuario()
                    usuarios.id = row[0]
                    usuarios.User_id = row[0]
                    usuarios.rut = row[7]
                    usuarios.fecha_ingreso = row[8]
                    usuarios.Area_id = int(row[9])
                    usuarios.Afp_id = row[10]
                    usuarios.Salud_id = row[11]
                    usuarios.CentroCosto_id = row[12]
                    usuarios.vencimiento_licencia_conducir = row[13]
                    usuarios.Cargo_id = row[14]
                    usuarios.save()
            return HttpResponseRedirect('/home')
    else:
        form = UploadFileForm()
    return render_to_response('cargar_usuarios.html', {'form': form}, context_instance=RequestContext(request))

@permission_required('portal.puede_cargar', login_url="/ingresar")  
def cargar_liquidaciones(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(request.FILES['docfile'])
            for row in reader:
                if row[0]=='usuario_rut':
                    print 'cabecera'
                else: 
                    liquidaciones = Liquidacion()
                    liquidaciones.Usuario_rut = row[0]
                    liquidaciones.mes = row[1]
                    liquidaciones.ano = row[2]
                    liquidaciones.porcentaje_cotizacion = row[3]
                    liquidaciones.pactado = row[4]
                    liquidaciones.tributable = row[5]
                    liquidaciones.dias_trabajados = row[6]
                    liquidaciones.sueldo = row[7]
                    liquidaciones.gratificacion = row[8]
                    liquidaciones.comision_produccion = row[9]
                    liquidaciones.semana_corrida = row[10]
                    liquidaciones.asignacion_viaticos = row[11]
                    liquidaciones.movilizacion_combustible = row[12]
                    liquidaciones.afp = row[13]
                    liquidaciones.adiciona_afp = row[14]
                    liquidaciones.salud = row[15]
                    liquidaciones.seguro_cesantia = row[16]
                    liquidaciones.anticipo = row[17]
                    liquidaciones.anticipo_combustible = row[18]
                    liquidaciones.anticipo_viatico = row[19]
                    liquidaciones.save()
            return HttpResponseRedirect('/home')
    else:
        form = UploadFileForm()
    return render_to_response('cargar_liquidaciones.html', {'form': form}, context_instance=RequestContext(request))