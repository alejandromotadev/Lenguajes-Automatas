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
    # variables = []
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
            file.write('-------------------------------------------------------LA CONSTRUCCION DEL PROYECTO--------------------------------------------------------------\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'EL DEBUG ESTA SENTENCIADO DE LA SIGUIENTE FORMA: {fileDFAdebug}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'LOS COMPONENTES Y MODULOS DEL PROYECTO: {fileDFAia}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'LOS HOSTS PERIMITDOS: {fileDFAah}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'LAS VARIABLES DE URL: {fileDFAurl}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'EL LANGUAGE CODE: {fileDFAlang}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
            file.write(f'LA BASES DE DATOS: {fileDFAdb}\n')
            file.write('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
button = Button(text='Abrir',command=abrir_archivo)
button.pack()
lblNombreArchivo=Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

window.mainloop()