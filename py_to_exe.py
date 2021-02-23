import os

file_path = input("Enter file name: ")
os.system(f"pyinstaller --hidden-import 'pygame' --onefile {file_path}")
