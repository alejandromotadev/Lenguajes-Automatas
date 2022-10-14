import debugDfa as dfaDebug
import installedAppsDfa as dfaIAPPS
import allowedH as dfaAH
import urlVarDfa as dfaUrl
import langDfa as dfaLanguage
from databasesDfa import declaracionDFA as dfaDB
from installedAppsDfa import declaracionDFA as dfaIA
   
def leerDebug():
    print('debuig leer')
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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
            
def leerInstalledApps():   
    print('installed apps leer')
    installedApps = ""
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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
    # with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
    #         data = infile.readline()
    #         print(data.strip())
    #         while data:     
    #             if dfaIAPPS.dfaIA.accepts_input(data.rstrip()):
    #                 print('aceptado\t')
    #                 # print(data.rstrip())
    #                 break
    #             else:
    #                 print('rechazado')
    #             data=infile.readline()
    #         print(data)
            
def leerAh():
    print('allowes hosts leer')
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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
            
def leerUrl():
    ('url variables leer')
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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
            
def leerLang():
    print('language leer')
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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
            
def leerDatabase():
    print('Base de datos leer')
    databases = ""
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
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