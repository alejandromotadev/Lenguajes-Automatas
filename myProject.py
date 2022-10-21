from automotadfa import declaracionDFA as dfaA

def leerAutomota(ruta):
    print('Leer Automata')
    dfa = ''
    with open(ruta, 'r') as infile:
        data = infile.readlines()
        for element in data:
            data[data.index(element)] = element.rstrip()  # limpia las lineas
        # concatena en una linea
        for linea in data[data.index('INSTALLED_APPS = ['):data.index(']')+1]:
            dfa += linea
             # concatena en una linea
        for linea in data[data.index('DEBUG = '):data.index('e')+1]:
            dfa += linea
        # concatena en una linea
        for linea in data[data.index('DATABASES = {'):data.index('}')+1]:
            dfa += linea
        # concatena en una linea
        for linea in data[data.index('ALLOWED_HOSTS = ['):data.index(']')+1]:
            dfa += linea
         # concatena en una linea
        for linea in data[data.index('DATABASES = {'):data.index('}')+1]:
            dfa += linea
            # concatena en una linea
        for linea in data[data.index('LANGUAGE_CODE = '):data.index("'")+1]:
            dfa += linea
            # concatena en una linea
        for linea in data[data.index('STATIC_URL = '):data.index("'")+1]:
            dfa += linea
             # concatena en una linea
        for linea in data[data.index('MEDIA_URL = '):data.index("'")+1]:
            dfa += linea
         # concatena en una linea
        for linea in data[data.index('STATIC_ROOT = '):data.index(')')+1]:
            dfa += linea
            # concatena en una linea
        for linea in data[data.index('MEDIA_ROOT = '):data.index(')')+1]:
            dfa += linea
        if dfaA().accepts_input(dfa):
            print('aceptado\t')
        else:
            data=infile.readline()
            print(data)
            dfaA().read_input(dfa)
            
        return dfa

def main():
    leerAutomota()

if __name__ == "__main__":
    main()
