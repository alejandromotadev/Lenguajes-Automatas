import debugDfa as dfaDebug
import installedAppsDfa as dfaIAPPS
import allowedH as dfaAH
import urlVarDfa as dfaUrl
import langDfa as dfaLanguage
from databasesDfa import declaracionDFA as dfaDB
from installedAppsDfa import declaracionDFA as dfaIA
   
def leerDebug(ruta):
    print('debuig leer')
    with open(ruta, 'r') as infile:
            data = infile.readline()
            print(data.strip())
            while data:     
                if dfaDebug.dfaDbg.accepts_input(data.strip()):
                    print('aceptado\t')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
            
def leerInstalledApps(ruta):   
    print('installed apps leer')
    installedApps = ""
    with open(ruta, 'r') as infile:
            data = infile.readlines()
            for element in data:
                data[data.index(element)] = element.rstrip() #limpia las lineas
            for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]: #concatena en una linea
                installedApps += linea
            if dfaIA().accepts_input(installedApps):
                print('aceptado\t') 
            else:
                print('rechazado')
                print(installedApps)
                dfaDB().read_input(installedApps)
            for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]: #concatena en una linea
                print(linea)
            
def leerAh(ruta):
    print('allowes hosts leer')
    with open(ruta, 'r') as infile:
            data = infile.readline()
            print(data.strip())
            while data:     
                if dfaAH.dfaAh.accepts_input(data.strip()):
                    print('aceptado\t')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                    
                data=infile.readline()
            print(data)
            
def leerUrl(ruta):
    ('url variables leer')
    with open(ruta, 'r') as infile:
            data = infile.readline()
            print(data.strip())
            while data:     
                if dfaUrl.dfaURL.accepts_input(data.strip()):
                    print('aceptado\t')
                    print(data.strip())
                else:
                   print('rechazado')
                data=infile.readline()
            print(data)
            
def leerLang(ruta):
    print('language leer')
    with open(ruta, 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaLanguage.dfaLg.accepts_input(data.strip()):
                    print('aceptado\t')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
            
def leerDatabase(ruta):
    print('Base de datos leer')
    databases = ""
    with open(ruta, 'r') as infile:
            data = infile.readlines()
            for element in data:
                data[data.index(element)] = element.rstrip() #limpia las lineas
            for linea in data[data.index('DATABASES = {'):data.index('}')+1]: #concatena en una linea
                databases += linea
            if dfaDB().accepts_input(databases):
                print('aceptado\t') 
            else:
                print('rechazado')
                print(databases)
                dfaDB().read_input(databases)
            for linea in data[data.index('DATABASES = {'):data.index('}')+1]: #concatena en una linea
                print(linea)
        
def main():
    leerDebug()
    leerInstalledApps()
    leerAh()
    leerUrl()
    leerLang()
    leerDatabase()
if __name__ == "__main__":
    main()