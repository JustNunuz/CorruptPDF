import os
import struct
import random
from PyPDF2 import PdfReader

def corrupt_pdf(input_file, output_file):
    input_path, input_filename = os.path.split(input_file)
    output_path, output_filename = os.path.split(output_file)

    with open(input_file, mode="rb") as f:
        raw_bytes = f.read()

    padding_length = random.randint(1 << 20, 5 << 20)

    with open(output_file, mode="wb") as f:
        f.write(struct.pack("<Q", padding_length))
        f.write(os.urandom(padding_length))

    with open(output_file, mode="ab") as f:
        f.write(raw_bytes)

    with open(output_file, mode="rb+") as f:
        f.seek(0)
        f.truncate()

current_dir = os.getcwd()
corrupt_pdf(os.path.join(current_dir, "original.pdf"), os.path.join(current_dir, "corrupted.pdf"))
print("OPERATION COMPLETED")