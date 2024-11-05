import PyPDF2
import os

os.chdir('C:\\Users\\NM Siddharth\\Desktop')

pdfFile = open('meetingminutes1.pdf','rb')
#print(pdfFile)
reader = PyPDF2.PdfReader(pdfFile)
pages = len(reader.pages)
print(pages)

# To extract text from specified page
first_page = reader.pages[0]  # Starts from 0
first_page_text = first_page.extract_text()
#print(first_page_text)

# To get text from whole pdf
for pageNum in range(len(reader.pages)):
    print(pageNum,reader.pages[pageNum].extract_text())
