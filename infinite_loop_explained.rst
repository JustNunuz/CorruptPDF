Title: Corrupting PDF Files with JavaScript Infinite Loop
========================================================

This reStructuredText (RST) file provides an explanation and documentation for a Python script that demonstrates how to corrupt a PDF file by adding a JavaScript code snippet that runs an infinite loop. The script uses the `reportlab` and `PyPDF2` libraries to create and modify the PDF file.

Code Overview
-------------

The script consists of two functions: `create_pdf` and `add_infinite_loop_js`.

1. `create_pdf(path)`: This function creates a new PDF file with a single page containing a text string. The path parameter specifies the output file path.

2. `add_infinite_loop_js(input_pdf, output_pdf)`: This function takes an existing PDF file as input and adds a JavaScript code snippet that runs an infinite loop to the file. The input_pdf parameter specifies the path to the existing PDF file, and the output_pdf parameter specifies the path to the output file.

Corrupting the PDF File
-----------------------

The script first creates a new PDF file using the `create_pdf` function. Then, it adds a JavaScript code snippet that runs an infinite loop to the PDF file using the `add_infinite_loop_js` function. The resulting PDF file will cause a browser or PDF viewer to hang or crash when opened, as the infinite loop will consume all available resources.

Usage
-----

To use this script, follow these steps:

1. Install the required libraries: `reportlab` and `PyPDF2`.
2. Run the script.
3. The script will create a new PDF file named "example.pdf" and then add a JavaScript code snippet that runs an infinite loop to the file, creating a new PDF file named "infinite_loop.pdf".
4. Open the "infinite_loop.pdf" file with a PDF viewer to see the corruption in action.

Disclaimer
-- The authors and contributors of this script do not condone or promote any illegal or unethical activities. The script should not be used to create malicious or harmful PDF files.