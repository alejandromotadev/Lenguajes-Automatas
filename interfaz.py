from tkinter import Entry, filedialog
from myProject import leerAutomota
from tkinter import *
import os

window = Tk()
window.title("Construccion del Django :D")
window.geometry('400x200')
ruta_str = "Ruta: "


def abrir_archivo():
    file = filedialog.askopenfilename(
        title="Abrir", initialdir="./", filetypes=(("Archivos .txt", "*.txt"), ("Archivos .py", "*.py")))
    if file is None:
        return 
    fileDFA = leerAutomota(file)
    name = nombreArchivo.get()
    ins = fileDFA[0].split(',')
    db = fileDFA[1].split(',')
    if os.path.exists(name+'.txt'):
        os.remove(name+'.txt')
    else:
        with open('./reportes/'+name+'.txt', 'w') as file:
            file.write('-------------------------------------------------------LA CONSTRUCCION DEL PROYECTO--------------------------------------------------------------\n')
            file.write(f'DJANGO SETTINGS : \n MODULOS Y COMPONENTES: \n')
            for i in ins:
                file.write(i + '\n')
            file.write('\n')
            file.write(f'DATABASES: \n')
            for i in db:
                file.write(i + '\n')
            file.write('\n')
            file.write(f'ALLOWED_HOSTS: \n{fileDFA[2]}\n')
            file.write('\n')
            file.write(f'DEBUG: \n{fileDFA[3]}\n')
            file.write('\n')
            file.write(f'URL STATIC: \n{fileDFA[4]}\n')
            file.write('\n')
            file.write(f'URL_MEDIA: \n{fileDFA[5]}\n')
            file.write('\n')
            file.write(f'LANGUAGE CODE: \n{fileDFA[6]}\n')

button = Button(text='Abrir', command=abrir_archivo)
button.pack()
lblNombreArchivo = Label(text="Nombre del archivo: ").pack()
nombreArchivo = Entry()
nombreArchivo.pack()

window.mainloop()
