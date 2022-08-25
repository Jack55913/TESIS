import os

os.system('pdflatex -interaction=nonstopmode main.tex')
os.system('pythontex.exe main.tex')
os.system('pdflatex -interaction=nonstopmode main.tex')