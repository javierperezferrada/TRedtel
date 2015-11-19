from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.http import HttpResponse

def PdfMuestra(request):
	respuesta = HttpResponse(content_type = 'application/pdf')
	respuesta['Content-Disposition'] = 'filename = "respuesta.pdf"'

	Temp = StringIO()

	Q = SimpleDocTemplate(Temp,rightMargin=72,leftMargin=72,topMargin=72,BottomMargin=18)


	Story = []

	styles = getSampleStyleSheet()

	ptext = 'Texto de prueba.'

	Story.append(Paragraph(ptext,styles["Normal"]))


	ptext = 'Usuario en el sistema es pura shit'

	Story.append(Paragraph(ptext,styles["Normal"]))

	Q.build(Story)

	respuesta.write(Temp.getvalue())

	Temp.close()

	return respuesta