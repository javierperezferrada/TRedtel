from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.http import HttpResponse

def PdfMuestra(request):
	respuesta = HttpResponse(content_type = 'application/pdf')
	respuesta['Content-Disposition'] = 'attachment; filename = "respuesta.pdf"'
	Q = SimpleDocTemplate(respuesta,rightMargin=72,leftMargin=72,topMargin=72,BottomMargin=18)

	Story = []

	styles = getSampleStyleSheet()

	ptext = 'Texto de prueba.'

	Story.append(Paragraph(ptext,styles["Normal"]))


	ptext = 'Usuario en el sistema es pura shit'

	Story.append(Paragraph(ptext,styles["Normal"]))

	Q.build(Story)
	return Q