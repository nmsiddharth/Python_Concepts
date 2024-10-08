import PyPDF2

f = open("E:\\SIDDU\\Technical\\Python\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\Working_Business_Proposal.pdf",'rb')

pdf_reader = PyPDF2.PdfReader(f)
page_one = pdf_reader.pages[0]
print(page_one)

# Extracted Text
page_one_extracted = page_one.extract_text()
print(page_one_extracted)

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)

pdf_output = open("new_PDF.pdf",'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()


