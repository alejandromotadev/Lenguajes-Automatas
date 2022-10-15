from tkinter import Entry, filedialog
from myProject import leerDebug,leerInstalledApps,leerAh,leerUrl,leerLang,leerDatabase
from tkinter import *
import os

window = Tk()
window.title("Construccion del Django")
window.geometry('200x200')
ruta_str = "Ruta: "
def abrir_archivo():
    file = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Archivos .txt", "*.txt"), ("Archivos .py", "*.py")))
    if file is None:
        return
    fileDFAdebug = leerDebug(file)
    fileDFAia = leerInstalledApps(file)
    fileDFAah = leerAh(file)
    fileDFAurl = leerUrl(file)
    fileDFAlang = leerLang(file)
    fileDFAdb = leerDatabase(file)
    name = nombreArchivo.get()
    if os.path.exists(name+'.txt'):
        os.remove(name+'.txt')
    else:
        with open('./reportes/'+name+'.txt', 'w') as file:
            file.write(fileDFAdebug)
            file.write(fileDFAia)
            file.write(fileDFAah)
            file.write(fileDFAurl)
            file.write(fileDFAlang)
            file.write(fileDFAdb)
button = Button(text='Abrir',command=abrir_archivo)
button.pack()
lblNombreArchivo=Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

window.mainloop()