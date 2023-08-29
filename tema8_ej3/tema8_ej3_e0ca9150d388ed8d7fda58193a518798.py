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
    copia = frase
    copia = copia.replace(',','')
    copia = copia.replace(':','')
    copia = copia.replace(';','')
    copia = copia.replace('.','')
    copia = copia.replace('!','')
    copia = copia.replace('¡','')
    copia = copia.replace('¿','')
    copia = copia.replace('?','')
    copia = copia.replace('(','')
    copia = copia.replace(')','')

    #numero de palabras
    splitted = copia.split()
    #print(splitted)
    #print("Número de palabras: %d" %len(splitted))

    #numero de caracteres
    caracteres = len(frase)

    #largo promedio de palabras
    largo_total_palabras = 0
    for palabra in splitted:
        largo_total_palabras = largo_total_palabras + len(palabra)

    promedio = largo_total_palabras / len(splitted)
    #print(largo_total_palabras)

    espacios = frase.count(' ')

    caracteres_especiales = 0
    caracteres_especiales = caracteres_especiales + frase.count('.')
    
    return len(splitted), caracteres, promedio, espacios, caracteres_especiales
