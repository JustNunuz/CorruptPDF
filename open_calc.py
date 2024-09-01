import os

def open_file(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Error: {e}")

file_path = "C:\\Windows\\System32\\calc.exe"
open_file(file_path)