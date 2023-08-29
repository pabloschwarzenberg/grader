import string

def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)
    numero_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = numero_caracteres / numero_palabras

    numero_espacios = s.count(" ")

    caracteres_puntuacion = set(string.punctuation)
    caracteres_letras_espacios = set(string.ascii_letters + " ")
    numero_puntuacion = sum(1 for char in s if char in caracteres_puntuacion and char not in caracteres_letras_espacios)

    return numero_palabras, numero_caracteres, largo_promedio, numero_espacios, numero_puntuacion

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

if __name__ == "__main__":
    resultado = estadisticas_frase(hombre_imaginario)
    print("Número de palabras:", resultado[0])
    print("Número de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])



         