import debugDfa as dfaDebug
import installedAppsDfa as dfaIAPPS
import allowedH as dfaAH
import urlVarDfa as dfaUrl
import langDfa as dfaLanguage
from databasesDfa import declaracionDFA as dfaDB
from installedAppsDfa import declaracionDFA as dfaIA
   
def leerDebug(ruta):
    print('debuig leer')
    debug = ''
    with open(ruta, 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaDebug.dfaDbg.accepts_input(data.strip()):
                    print('aceptado\t')
                    debug += data.strip()
                    break
                else:
                    pass
                data=infile.readline()
            return debug
            
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
                dfaDB().read_input(installedApps)
            for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]: #concatena en una linea
                print(linea)
            return installedApps
            
def leerAh(ruta):
    print('allowes hosts leer')
    allow_host = ''
    with open(ruta, 'r') as infile:
            data = infile.readline()
            print(data.strip())
            while data:     
                if dfaAH.dfaAh.accepts_input(data.strip()):
                    print('aceptado\t')
                    allow_host+=data.strip()
                    break
                else:
                    pass
                data=infile.readline()
            return allow_host
            
def leerUrl(ruta):
    ('url variables leer')
    url_variables = ''
    with open(ruta, 'r') as infile:
            data = infile.readline()
            print(data.strip())
            while data:     
                if dfaUrl.dfaURL.accepts_input(data.strip()):
                    print('aceptado\t')
                    url_variables+=data.strip()
                else:
                   pass
                data=infile.readline()
            return url_variables
            
def leerLang(ruta):
    print('language leer')
    lenguage_code = ''
    with open(ruta, 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaLanguage.dfaLg.accepts_input(data.strip()):
                    print('aceptado\t')
                    lenguage_code += data.strip()
                    break
                else:
                    pass
                data=infile.readline()
            return lenguage_code
            
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
                dfaDB().read_input(databases)
            for linea in data[data.index('DATABASES = {'):data.index('}')+1]: #concatena en una linea
                print(linea)
            return databases
        
def main():
    leerDebug()
    leerInstalledApps()
    leerAh()
    leerUrl()
    leerLang()
    leerDatabase()
if __name__ == "__main__":
    main()