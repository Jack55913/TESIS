import os

# os.system('pdflatex -interaction=nonstopmode main.tex')
# os.system('pythontex.exe main.tex')
# os.system('pdflatex -interaction=nonstopmode main.tex')

os.system('pdflatex -shell-escape main.tex')
os.system('biber main')
os.system('pdflatex -shell-escape main.tex')
os.system('pdflatex -shell-escape main.tex')