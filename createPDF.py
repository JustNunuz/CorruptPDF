#File works

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    c.drawString(100, 750, "Hello, this is a PDF document created with ReportLab!")
    c.drawString(100, 730, "PyPDF2 is primarily used for manipulating PDFs, not creating them.")
    c.drawString(100, 710, "We are creating this PDF with ReportLab and will manipulate it with PyPDF2.")

    c.save()

create_pdf("example.pdf")
