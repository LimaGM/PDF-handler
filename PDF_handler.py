from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('PDF Handler')
myLabel = Label(root, text='PDF Handler 0.1').grid(row=0, column=1, padx=70)
myLabel2 = Label(root, text='').grid(row=0, column=0, pady=20)
myLabel3 = Label(root, text='').grid(row=0, column=2, pady=20)

myLabel4 = Label(root, text='').grid(row=3, column=1, pady=20)
results = Label(root, text='')
results.grid(row=3, column=1, pady=20)

def merge():
    global results
    results.destroy()
    paths = filedialog.askopenfilenames(
        initialdir='C:\\', title='Select a File', filetypes=(('PDF files', '*pdf'), ('All files', '*.*')))
    fname = 'yourmergedfiles'

    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    try:
        os.mkdir(str(os.path.dirname(paths[0])) + '/yourmerge/')
    except:
        pass
    a = str(os.path.dirname(paths[0])) + '/yourmerge/'

    with open(a + fname+'.pdf', 'wb') as out:
        pdf_writer.write(out)

    results = Label(root, text='Files were successfully created')
    results.grid(row=3, column=1, pady=20)

def split():
    global results
    results.destroy()
    path = filedialog.askopenfilename(
        initialdir='C:\\', title='Select a File', filetypes=(('PDF files', '*pdf'), ('All files', '*.*')))
    fname = os.path.basename(path)
    pdf = PdfFileReader(path)
    a = str(os.path.dirname(path)) + '/yoursplit/'
    try:
        os.mkdir(str(os.path.dirname(path)) + '/yoursplit/')
    except:
        pass
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        with open(a + fname + f'{page}.pdf', 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
    results = Label(root, text='Files were successfully created')
    results.grid(row=3, column=1, pady=20)



myButton = Button(root, text='Split', command=split).grid(row=1, column=1, pady=10)
myButton2 = Button(root, text='Merge', command=merge).grid(row=2, column=1, pady=10)

root.mainloop()
