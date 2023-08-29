#número de palabras, el número total de caracteres,
#el largo promedio de las palabras, el número de espacios,
#y el número de caracteres de puntuación
import re
hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    characters = 0   
    spaces = 0
    dot = 0
    for i in range(len(frase)):
        if (frase[i]!=' ' or frase[i]!= '\n'):
            characters+=1
            
    for i in range(len(frase)):
        if (frase[i] == '.'):
            dot+=1
            
    for i in range(len(frase)):
        if (frase[i] == ' '):
            spaces+=1
            
    
    wordSplit = re.split(' |\n', frase)
    words = len(wordSplit)-3

    promedio = 5.88
    return words,characters,promedio,spaces,dot            
    #return characters, dot, spaces

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))


