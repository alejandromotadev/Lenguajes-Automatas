import debugDfa as dfaDebug
import installedAppsDfa as dfaIAPPS
import allowedH as dfaAH
import urlVarDfa as dfaUrl
import langDfa as dfaLanguage
import databasesDfa as dfaDB
   
def leerDebug():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaDebug.dfaDbg.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
def leerInstalledApps():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaIAPPS.dfaIA.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
def leerAh():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaAH.dfaAh.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
def leerUrl():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaUrl.dfaURL.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
def leerLang():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaLanguage.dfaLg.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                    break
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
def leerDatabase():
    with open('./ejemplos/ejemplo 1.txt', 'r') as infile:
            data = infile.readline()
            while data:     
                if dfaDB.dfaDb.accepts_input(data.strip()):
                    print('aceptado\n')
                    print(data.strip())
                else:
                    print('rechazado')
                data=infile.readline()
            print(data)
        
def main():
    leerDebug()
    leerInstalledApps()
    leerAh()
    leerUrl()
    leerLang()
    leerDatabase()
if __name__ == "__main__":
    main()
    
