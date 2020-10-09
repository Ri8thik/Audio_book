import pyttsx3
import PyPDF2
book =open("oops.pdf",'rb')
pdf_read=PyPDF2.PdfFileReader(book)
##n to print the no of pages of the pdf  
pages=pdf_read.numPages
print(pages)

speaker = pyttsx3.init()
for i in range(21,pages):
    page=pdf_read.getPage(i)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()