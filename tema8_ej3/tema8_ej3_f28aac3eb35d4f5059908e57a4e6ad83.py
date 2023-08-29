import string

def estadisticas_frase(frase):
    # Número de palabras
    palabras = frase.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(frase)

    # Largo promedio de las palabras
    suma_largos = sum(len(palabra) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras if num_palabras > 0 else 0

    # Número de espacios
    num_espacios = frase.count(" ")

    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_caracteres_puntuacion = sum(1 for char in frase if char in caracteres_puntuacion)

    return {
        "Número de palabras": num_palabras,
        "Número total de caracteres": num_caracteres,
        "Largo promedio de las palabras": largo_promedio,
        "Número de espacios": num_espacios,
        "Número de caracteres de puntuación": num_caracteres_puntuacion
    }

if __name__ == "__main__":
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

    resultado = estadisticas_frase(hombre_imaginario)
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")      