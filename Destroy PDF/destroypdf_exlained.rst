Title: Corrupting PDF Files by Padding with Random Bytes
=====================================================================

This reStructuredText (RST) file provides an explanation and documentation for a Python script that demonstrates how to corrupt a PDF file by padding it with random bytes. The script uses the `PyPDF2` library to read the input PDF file and the `os` and `struct` libraries to write the corrupted PDF file.

Code Overview
-------------

The script consists of a single function: `corrupt_pdf(input_file, output_file)`.

1. `corrupt_pdf(input_file, output_file)`: This function takes an existing PDF file as input and corrupts it by padding it with random bytes. The input_file parameter specifies the path to the existing PDF file, and the output_file parameter specifies the path to the output file.

Corrupting the PDF File
-----------------------

The script reads the input PDF file and stores its contents as a byte string. It then generates a random padding length between 1MB and 5MB. The script writes the padding length as a little-endian unsigned long long integer to the output file, followed by the specified number of random bytes. Finally, the script appends the contents of the input PDF file to the output file and truncates the file to the length of the input file.

Usage
-----

To use this script, follow these steps:

1. Install the required library: `PyPDF2`.
2. Place the input PDF file in the same directory as the script.
3. Run the script.
4. The script will create a new PDF file named "corrupted.pdf" in the same directory as the input file.
5. Open the "corrupted.pdf" file with a PDF viewer to see the corruption in action.

Disclaimer
----------

This script is intended for educational purposes only. The authors and contributors of this script do not condone or promote any illegal or unethical activities. The script should not be used to create malicious or harmful PDF files.