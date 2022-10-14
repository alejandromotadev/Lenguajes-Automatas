from tkinter import Entry, filedialog
from tkinter.ttk import Treeview
from myProject import leerDebug,leerInstalledApps,leerAh,leerUrl,leerLang,leerDatabase
from tkinter import Tk,Frame, END, Label, CENTER, Button, Text
import os

installed_apps = ''
databases = ''
debug = ''
allow_host = ''
url_variable = ''
language_code = ''

window = Tk()
window.minsize(width=600, height=600)
window.title("Construccion del Django")
window.geometry('600x600')
ruta_str = "Ruta: "
def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Archivos .txt", "*.txt"), ("Archivos .py", "*.py")))
    installed_apps = leerInstalledApps(archivo)
    databases = leerDatabase(archivo)
    debug = leerDebug(archivo)
    allow_host = leerAh(archivo)
    url_variable = leerUrl(archivo)
    language_code = leerLang(archivo)
def crear_reporte():
    name = nombreArchivo.get()
    if os.path.exists(name+'.txt'):
        os.remove(name+'.txt')
    else:
        with open('./reportes/'+name+'.txt', 'w') as f:
            f.write(installed_apps)
            f.write(databases)
            f.write(debug)
            f.write(allow_host)
            f.write(url_variable)
            f.write(language_code)
btnSave = Button(window, text="Open", command=abrir_archivo)
btnSave.pack()

lblNombreArchivo=Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

btnSave = Button(window, text="Save", command=crear_reporte)
btnSave.pack()

window.mainloop()