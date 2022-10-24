from automotadfa import declaracionDFA, example

def leerAutomota(ruta):
    print('Leer Automata')
    dfa = ''
    with open(ruta, 'r') as infile:
        data = infile.readlines()
        if declaracionDFA().accepts_input(dfa):
            print('aceptado\t')
            for element in data:
                data[data.index(element)] = element.rstrip()  # limpia las lineas

            for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]:
                dfa += linea
                dfa += '\n'
                    
            for linea in data[data.index('DATABASES = {'):data.index('}')+1]:
                dfa += linea
                dfa += '\n'
            for linea in data:
                if 'DEBUG' in linea:
                    dfa += linea 
                    dfa += '\n'
            for linea in data:
                if 'ALLOWED_HOSTS' in linea:
                    dfa += linea 
                    dfa += '\n'
            for linea in data:
                if 'LANGUAGE_CODE' in linea:
                    dfa += linea 
                    dfa += '\n'
            for linea in data:
                if 'STATIC' in linea:
                    dfa += linea 
                    dfa += '\n'
            for linea in data:
                if 'MEDIA' in linea:
                    dfa += linea 
                    dfa += '\n'
            return dfa
        else:
            print('rechazado')
            print(dfa)
            example(dfa)
            declaracionDFA().read_input(dfa)
       
def main():
    leerAutomota()

if __name__ == "__main__":
    main()
