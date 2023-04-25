# -*- coding: utf8 -*-
from PyPDF2 import PdfMerger# PdfFileMerger 
import os
files = os.listdir()
pdfs = [] 
for pdf in files:
    if pdf[-4:].lower() == '.pdf':
        pdfs.append(pdf)
merger = PdfMerger() 
for pdf in pdfs:
    merger.append(pdf) 
merger.write("!_Чертежи PDF (все в одном).pdf") 
