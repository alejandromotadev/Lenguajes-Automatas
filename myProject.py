from automotadfa import declaracionDFA, example

def leerAutomota(ruta):
    print('Leer Automata')
    dfaINS = ''
    dfaDATA = ''
    dfaDEBG = ''
    dfaALLW = ''
    dfaLANG = ''
    dfaSTC = ''
    dfaMED = ''
    with open(ruta, 'r') as infile:
        data = infile.readlines()
        for element in data:
            data[data.index(element)] = element.rstrip()  # limpia las lineas
        for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]:
            dfaINS += linea   
        for linea in data[data.index('DATABASES = {'):data.index('}')+1]:
            dfaDATA += linea
        for linea in data:
            if 'DEBUG' in linea:
                dfaDEBG += linea 
        for linea in data:
            if 'ALLOWED_HOSTS' in linea:
                dfaALLW += linea 
        for linea in data:
            if 'LANGUAGE_CODE' in linea:
                dfaLANG += linea 
        for linea in data:
            if 'STATIC' in linea:
                dfaSTC += linea 
        for linea in data:
            if 'MEDIA' in linea:
                dfaMED += linea 
                
        if declaracionDFA().accepts_input(dfaINS):
            print('aceptado installed apps\t')
            
        else:
            print('rechazado installed apps')
            example(dfaINS)
            declaracionDFA().read_input(dfaINS)  
        
        if declaracionDFA().accepts_input(dfaDATA):
            print('aceptado databases\t')
            
        else:
            print('rechazado databases')
            example(dfaDATA)
            declaracionDFA().read_input(dfaDATA)
            
        if declaracionDFA().accepts_input(dfaDEBG):
            print('aceptado debug\t')
           
        else:
            print('rechazado debug')
            example(dfaDEBG)
            declaracionDFA().read_input(dfaDEBG)
            
        if declaracionDFA().accepts_input(dfaALLW):
            print('aceptado allowed hosts\t')
          
        else:
            print('rechazado allowed hosts')
            example(dfaALLW)
            declaracionDFA().read_input(dfaALLW)
            
        if declaracionDFA().accepts_input(dfaLANG):
            print('aceptado language code\t')     
        else:
            print('rechazado language code')
            example(dfaLANG)
            declaracionDFA().read_input(dfaLANG)
            
        if declaracionDFA().accepts_input(dfaSTC):
            print('aceptado url variable static\t')
           
        else:
            print('rechazado url variable static')
            example(dfaSTC)
            declaracionDFA().read_input(dfaSTC)
            
        if declaracionDFA().accepts_input(dfaMED):
            print('aceptado url variable media\t')
           
        else:
            print('rechazado url variable media')
            example(dfaMED)
            declaracionDFA().read_input(dfaMED)
        return dfaINS, dfaDATA, dfaALLW, dfaDEBG, dfaSTC, dfaMED, dfaLANG
        
def main():
    leerAutomota()

if __name__ == "__main__":
    main()
