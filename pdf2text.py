import PyPDF2

pdfFileObj = open('/home/iqra/Downloads/abc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for i in range()
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)
