import string

def estadisticas_frase(frase):
    palabras = frase.split()
    numero_palabras = len(palabras)
    numero_caracteres = len(frase)
    largo_promedio_palabras = sum(len(palabra.strip(string.punctuation)) for palabra in palabras) / numero_palabras
    numero_espacios = frase.count(' ')
    caracteres_puntuacion = sum(caracter in string.punctuation for caracter in frase if caracter != ' ')
    
    return (numero_palabras, numero_caracteres, round(largo_promedio_palabras, 2), numero_espacios, caracteres_puntuacion)

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
    estadisticas = estadisticas_frase(hombre_imaginario)
    print(estadisticas)
