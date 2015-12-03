# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Image, Table
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from django.http import HttpResponse



#   try: 
#        usuario = get_object_or_404(Usuario, id=request.user.id)
#    except ValueError: 
#        raise Http404() 
#    respuesta = HttpResponse(content_type = 'application/pdf')
#    respuesta['Content-Disposition'] = 'filename = "respuesta.pdf"'

# Para agregar a views.py, eliminar comentarios de la parte de arriba y reemplazar 
# "PentaDurr.pdf" con respuesta, tambien, agregar

#    respuesta.close()

#    return respuesta

Q = SimpleDocTemplate(respuesta,rightMargin=72,leftMargin=72,topMargin=72,BottomMargin=18)
Story = []

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Header',alignment=1,spaceBefore=85,fontSize=20,leading=22))
styles.add(ParagraphStyle(name='Estilo01',alignment = 2))
styles.add(ParagraphStyle(name='Estilo02',alignment = 0,firstLineIndent=100,spaceBefore=50,fontSize=18,leading=20))
styles.add(ParagraphStyle(name='Pie',spaceBefore=100,alignment=2))

ptext = 'Servicios e Ingenieria Ltda.'
ptext2 = 'Valdivia, Chile (Agregar fecha)'
pa = Paragraph(ptext,styles['Estilo01'])
pa2 = Paragraph(ptext2,styles['Estilo01'])
im = Image("Redtel_logo.gif")
im.halign="LEFT"

data = [[im,pa],['',pa2]]

TTemp = Table(data,colWidths=90*mm)

Story.append(TTemp)

HText = "CERTIFICADO"

Header = Paragraph(HText,styles['Header'])

Story.append(Header)

ptext = '<b>JULIO GUIDILFREDO ZARECHT ORTEGA</b>, rut 7.385,055-K representante legal de <b>Servicios e Ingenieria Limitada</b>,\
 Rut: 77.869.650-9 por medio de la presente, certifica que el señor NOMBRE_USUARIO, RUT: RUT_USUARIO, es trabajador de esta empresa, \
 se desempeña como Encargado RRHH, con contrato vigente desde el <b>FECHA_CONTRATO</b> y es de caracter <b>Indefinido</b>, y registra\
 domicilio según contrato en <b>DIRECCION</b>, de Valdivia'

TTemp = Paragraph(ptext,styles['Estilo02'])

Story.append(TTemp)

ptext = 'Se emite el presente certificado a peticion del interesado para ser presentadoen <b>AFP</b>'

TTemp = Paragraph(ptext,styles['Estilo02'])

Story.append(TTemp)

ptext = "JULIO GUIDILFREDO ZARECHT ORTEGA <br/> Representante Legal"

TTemp = Paragraph(ptext,styles['Pie'])

Story.append(TTemp)

Q.build(Story)