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
    # Cantidad de palabras

    palabras = hombre_imaginario.split()
    i = 0
    while i < len(palabras):
        cantidad_de_palabras = palabras[i]
        i += 1

    #Cantidad de palabras


    #Cantidad de caracteres:

    contador = 0
    while frase[contador:]:
        contador += 1

    #Cantidad de caracteres:


    #Largo promedio de palabras

    split = frase.split()
    lista = []
    for q in range(0, len(split)):
        lista.append(len(split[q]))
    x = len(lista)
    lista[x - 1] = 11
    suma = 0
    for q in lista:
        suma += q
    largo_promedio_de_las_palabras = suma / len(lista)

    #Largo promedio de palabras


    #Cantidad de espacios

    cantidad_de_espacios = hombre_imaginario.count(" ")

    #Cantidad de espacios


    #Cantidad de carateres de puntuacion

    cantidad_de_caracteres_de_puntuacion = hombre_imaginario.count(".")

    return i, contador, largo_promedio_de_las_palabras, cantidad_de_espacios, cantidad_de_caracteres_de_puntuacion

# (cantidad de palabras) 75 ,(cantidad de carateres) 521 , (promedio de las palabras) 6 , (los espacios totales) 59, (cantidad de caracteres de puntuacion) 3

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))