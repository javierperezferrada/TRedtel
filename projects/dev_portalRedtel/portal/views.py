# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO 
from reportlab.pdfgen import canvas
from .models import Usuario, Us
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
def us(request):
    us = Us.objects.get(id=1)
    return render_to_response('us.html', {'us': us}, context_instance=RequestContext(request))


@login_required()
def mis_datos(request):
	usuario = get_object_or_404(Usuario, id=request.user.id)
	return render_to_response('mis_datos.html', {'usuario': usuario}, context_instance=RequestContext(request))

#@login_required()
#def obtener_certificado(request):
#    usuario = get_object_or_404(Usuario, id=request.user.id)
#    return render_to_response('obtener_certificado.html', {'usuario': usuario}, context_instance=RequestContext(request))

@login_required()
def mis_liquidaciones(request):
    liquidaciones = Liquidacion.objects.filter(Usuario_rut=request.user.first_name)
    return render_to_response('mis_liquidaciones.html', {'liquidaciones': liquidaciones}, context_instance=RequestContext(request))

@login_required()
def liq_detalle(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    liquidaciones = Liquidacion.objects.filter(Usuario_rut=usuario.rut)
    return render_to_response('mis_liquidaciones.html', {'liquidaciones': liquidaciones}, context_instance=RequestContext(request))


@login_required()
def obtener_certificado(request):
    try: 
        usuario = get_object_or_404(Usuario, id=request.user.id)
    except ValueError: 
        raise Http404() 
    respuesta = HttpResponse(content_type = 'application/pdf')
    respuesta['Content-Disposition'] = 'filename = "Certificado_antiguedad_laboral.pdf"'
    Q = SimpleDocTemplate(respuesta,rightMargin=72,leftMargin=72,topMargin=72,BottomMargin=18)
    Story = []
    styles = getSampleStyleSheet()
    ptext = 'Texto de prueba.'
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Rut usuario: '+str(usuario.rut)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Fecha Ingreso: '+str(usuario.fecha_ingreso)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Vencimiento Licencia de Conducir: '+str(usuario.vencimiento_licencia_conducir)
    Story.append(Paragraph(ptext,styles["Normal"]))
    Q.build(Story)
    respuesta.close()
    return respuesta
 

@login_required()
def imprimir_liquidacion(request,pk):   
    try: 
        liquidacion = Liquidacion.objects.get(id=pk) 
    except ValueError: # Si no existe llamamos a "pagina no encontrada". 
        raise Http404()  
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = "attachment; filename="+str(liquidacion.mes)+"_"+str(liquidacion.ano)+".pdf"
    Q = SimpleDocTemplate(response,rightMargin=72,leftMargin=72,topMargin=72,BottomMargin=18)
    Story = []
    styles = getSampleStyleSheet()
    ptext = 'Liquidacion de Sueldo.'
    Story.append(Paragraph(ptext,styles["Normal"]))

    ptext = 'Rut Trabajador: '+str(liquidacion.Usuario_rut)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'mes: '+str(liquidacion.mes)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'año: '+str(liquidacion.ano)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'zonal: '+str(liquidacion.zonal)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'centro costo: '+str(liquidacion.c_costo)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'dias: '+str(liquidacion.dias)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Sueldo: '+str(liquidacion.sueldo)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Horas extras: '+str(liquidacion.h_extras)
    Story.append(Paragraph(ptext,styles["Normal"]))
    ptext = 'Bonos imponibles: '+str(liquidacion.bonos_impon)
    Story.append(Paragraph(ptext,styles["Normal"]))
    Q.build(Story)
    response.close()
    return response

@login_required()
def imprimir_ultima(request):  
    try: 
        usuario = get_object_or_404(Usuario, id=request.user.id)
        qs = Liquidacion.objects.filter(Usuario_rut=usuario.rut)
        qs = qs.latest("mes")
    except ValueError: 
        raise Http404() 
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    buffer = BytesIO() 
    p = canvas.Canvas(buffer) 
    p.drawString(100, 800, "Rut trabajador")
    p.drawString(300, 800, str(qs.Usuario_rut))
    p.drawString(100, 790, "mes")
    p.drawString(300, 790, str(qs.mes))
    p.drawString(100, 780, "Sueldo")
    p.drawString(300, 780, str(qs.sueldo))
    p.drawString(100, 770, "Gratificacion legal")
    p.drawString(300, 770, str(qs.gratificacion))
    p.drawString(100, 760, "AFP")
    p.drawString(300, 760, str(qs.afp))
    p.drawString(100, 750, "Anticipo")
    p.drawString(300, 750, str(qs.anticipo))
    p.showPage() 
    p.save() 
    pdf = buffer.getvalue() 
    buffer.close() 
    response.write(pdf) 
    return response

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
                        email=row[4],password=row[5]) 
                    usuarios = Usuario()
                    usuarios.id = row[0]
                    usuarios.User_id = row[0]
                    usuarios.rut = row[7]
                    usuarios.fecha_ingreso = row[8]
                    usuarios.area = row[9]
                    usuarios.afp = row[10]
                    usuarios.salud = row[11]
                    usuarios.ccosto = row[12]
                    usuarios.vencimiento_licencia_conducir = row[13]
                    usuarios.cargo = row[14]
                    usuarios.direccion = row[15]
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
            index = 0
            for index,row in enumerate(reader):
                if index<7:
                    print 'cabecera'
                else: 
                    liquidaciones = Liquidacion()
                    liquidaciones.Usuario_rut = row[1]
                    liquidaciones.mes = 'mayo'
                    liquidaciones.ano = 2015
                    liquidaciones.zonal = row[2]
                    liquidaciones.c_costo = row[3]
                    liquidaciones.dias = row[4]
                    liquidaciones.sueldo = row[5]
                    liquidaciones.h_extras = row[6]
                    liquidaciones.bonos_impon = row[7]
                    liquidaciones.gratificacion = row[8]
                    liquidaciones.total_impon = row[9]
                    liquidaciones.movilizacion = row[10]
                    liquidaciones.colacion = row[11]
                    liquidaciones.otros_no_impon = row[12]
                    liquidaciones.asig_fam = row[13]
                    liquidaciones.total_no_impon = row[14]
                    liquidaciones.total_haberes = row[15]
                    liquidaciones.afp = row[16]
                    liquidaciones.seg_cesantia = row[17]
                    liquidaciones.anticipo_combustible = row[18]
                    liquidaciones.sis = row[19]
                    liquidaciones.ahorro_afp = row[20]
                    liquidaciones.salud = row[21]
                    liquidaciones.mutual = row[22]
                    liquidaciones.impto_unico = row[23]
                    liquidaciones.prestamo_ccaf = row[24]
                    liquidaciones.prestamos = row[25]
                    liquidaciones.anticipos = row[26]
                    liquidaciones.otros_dsctos = row[27]
                    liquidaciones.total_dsctos = row[28]
                    liquidaciones.liquido_pago = row[29]
                    liquidaciones.save()
            return HttpResponseRedirect('/home')
    else:
        form = UploadFileForm()
    return render_to_response('cargar_liquidaciones.html', {'form': form}, context_instance=RequestContext(request))
