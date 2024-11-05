import PyPDF2
import os

from Automation.combining_2_PDFs import writer

os.chdir('D:\\SIDDU\\Resume')

pdfFile1 = open('NM Siddharth _Resume.pdf','rb')
pdfFile2 = open('NM Siddharth _Resume.pdf','rb')

reader1 = PyPDF2.PdfReader(pdfFile1)
reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

output_file = open('combined_resume.pdf','wb')
writer.write(output_file)
output_file.close()
pdfFile1.close()
pdfFile2.close()