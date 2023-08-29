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
    cantidad_palabras = 0
    cantidad_total_caracteres = 0
    cantidad_caracteres_puntuacion = 0
    largo_promedio_palabra = 0
    cantidad_espacio = frase.count(" ")
    arreglo_palabras = []
    contador_caracteres = 0
    suma = 0

    x = frase.split ( )
    
    for palabra in x:

        if  palabra.count(".") == 0 and palabra.count(",") == 0:
            cantidad_palabras = cantidad_palabras + 1
            cantidad_total_caracteres = cantidad_total_caracteres + len (palabra)
            arreglo_palabras.append(len (palabra))
        elif len (palabra) >1 and palabra.count(".") > 0:
            cantidad_palabras = cantidad_palabras + 1
            cantidad_total_caracteres = cantidad_total_caracteres + (len(palabra.replace(".","")))
            arreglo_palabras.append(len(palabra.replace(".","")))
            cantidad_caracteres_puntuacion = cantidad_caracteres_puntuacion + palabra.count(".")
        elif palabra == "." or palabra == ",":
            cantidad_caracteres_puntuacion += 1

    largo_promedio_palabra = cantidad_total_caracteres / cantidad_palabras

    return (len(arreglo_palabras), (len(frase)), largo_promedio_palabra, cantidad_espacio,cantidad_caracteres_puntuacion)
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         