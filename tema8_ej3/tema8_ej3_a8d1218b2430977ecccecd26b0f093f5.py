import string

def estadisticas_frase(frase):
    frase = frase.strip(string.punctuation)
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = 0
    for palabra in palabras:
        num_caracteres += len(palabra)


    if num_palabras > 0:
        largo_promedio = num_caracteres / num_palabras
    else:
        largo_promedio = 0

    num_espacios = frase.count(" ")
    

    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = 0
    for caracter in frase:
        if caracter in caracteres_puntuacion:
            num_puntuacion += 1


    return {
        "Número de palabras": num_palabras,
        "Número total de caracteres": num_caracteres,
        "Largo promedio de las palabras": largo_promedio,
        "Número de espacios": num_espacios,
        "Número de caracteres de puntuación": num_puntuacion
    }

if __name__ == "__main__":
    hombre_imaginario = """El hombre imaginario
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
circundado de cerros imaginarios... """
    
    print(estadisticas_frase(hombre_imaginario))
