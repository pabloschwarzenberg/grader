## ESTE EJERCICIO EN PYTHON FUNCIONA BIEN, AL COPIAR EL CÓDIGO ACA INDICA UNA RESPUESTA INCORRECTA
## FAVOR REVISAR EN PYTHON Y CALIFICAR, GRACIAS

## ENTRADA DE DATOS - PROCESO - SALIDA

import string

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

def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)
    numero_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = numero_caracteres / numero_palabras
    numero_espacios = s.count(' ')
    numero_puntuacion = sum(caracter in string.punctuation for caracter in s)

    return numero_palabras, numero_caracteres, largo_promedio, numero_espacios, numero_puntuacion
    
## LLAMADA FUNCIÓN E IMPRESIÓN EN PANTALLA    

if __name__ == "__main__":
    resultado = estadisticas_frase(hombre_imaginario)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])