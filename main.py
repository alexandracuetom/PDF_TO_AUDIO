import pyttsx3
import PyPDF2
from tkinter.filedialog import *


book = askopenfilename() #name of pdf file
pdfreader = PyPDF2.PdfReader(book)
page_num = len(pdfreader.pages)

player = pyttsx3.init()

#read data of pdf
for num in range(0, page_num):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player.say(text)

player.runAndWait()


