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
    nro_caracteres = len(frase)
    #nro de espacios
    espacios = frase.count(" ")
 #nro de caracteres de puntuación
    puntuacion = frase.count(".")+ frase.count(",")+ frase.count(";")
 #nro de palabras
    frase = frase.replace(",","")
    frase = frase.replace(";","")
    frase = frase.replace(".","")
    frase = frase.replace('\n', " ")
    palabras = frase.split(" ")
    print(palabras)
    nro_palabras = len(palabras)-3
 #nro de caracteres
 #largo promedio de las palabras
    suma = 0
    for palabra in palabras:
        no = len(palabra)
        suma+=no
    prom = suma/nro_palabras
    return nro_palabras, nro_caracteres, prom, espacios, puntuacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         