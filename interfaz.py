from tkinter import Entry, filedialog
from myProject import leerAutomota
from tkinter import *
import os

window = Tk()
window.title("Construccion del Django")
window.geometry('200x200')
ruta_str = "Ruta: "


def abrir_archivo():
    file = filedialog.askopenfilename(
        title="Abrir", initialdir="./", filetypes=(("Archivos .txt", "*.txt"), ("Archivos .py", "*.py")))
    if file is None:
        return
    fileDFA = leerAutomota(file)
    name = nombreArchivo.get()
    if os.path.exists(name+'.txt'):
        os.remove(name+'.txt')
    else:
        with open('./reportes/'+name+'.txt', 'w') as file:
            file.write('-------------------------------------------------------LA CONSTRUCCION DEL PROYECTO--------------------------------------------------------------\n')
            file.write(f'DJANGO SETTINGS: {fileDFA}\n')


button = Button(text='Abrir', command=abrir_archivo)
button.pack()
lblNombreArchivo = Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

window.mainloop()
