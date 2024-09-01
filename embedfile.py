from PyPDF2 import PdfReader, PdfWriter

# Create a new PDF writer
pdf_writer = PdfWriter()

# Add a page to the PDF
pdf_writer.add_page(PdfReader("Corrupt PDF\\original.pdf").pages[0])

# Embed the file
embedded_file = pdf_writer.add_embedded_file("calc.exe", "application/octet-stream")

# Add an annotation to the page
annotation = pdf_writer.add_annotation("/Annot", "/S/EmbeddedFile", embedded_file)

# Save the PDF
with open("embedded_file_pdf.pdf", "wb") as out_pdf:
    pdf_writer.write(out_pdf)