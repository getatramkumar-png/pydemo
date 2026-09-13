import os
from pathlib import Path
os.system("cls")

print(Path(__file__)) 

file_path = Path(__file__).resolve().parent.parent / "doc/demo.txt"
print(file_path)
with file_path.open("r", encoding="utf-8") as file:
	print(file.read())

with open("C:/Users/Ramkumar/pydemo/src/pydemo/doc/demo.txt","r") as fs:
		  print(fs.read())
"""
with open("../doc/demo.txt","r") as fss:
	print(fss.read())


file= open("../doc/demo.txt","r")
print(file.read())
file.close()"""