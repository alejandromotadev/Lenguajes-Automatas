from tkinter import Entry, filedialog
from tkinter.ttk import Treeview
from myProject import leerDebug,leerInstalledApps,leerAh,leerUrl,leerLang,leerDatabase
from tkinter import Tk,Frame, END, Label, CENTER, Button, Text
import os

window = Tk()
window.minsize(width=600, height=600)
window.title("Construccion del Django")
window.geometry('600x600')
ruta_str = "Ruta: "
def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Archivos .txt", "*.txt"), ("Archivos .py", "*.py")))
    leerInstalledApps(archivo)
    leerDatabase(archivo)
    leerDebug(archivo)
    leerAh(archivo)
    leerUrl(archivo)
    leerLang(archivo)
def crear_reporte():
    name = nombreArchivo.get()
    if os.path.exists(name+'.txt'):
        os.remove(name+'.txt')
    else:
        with open('./reportes/'+name+'.txt', 'w') as f:
            f.write()
btnSave = Button(window, text="Open", command=abrir_archivo)
btnSave.pack()

lblNombreArchivo=Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

btnSave = Button(window, text="Save", command=crear_reporte)
btnSave.pack()

window.mainloop()