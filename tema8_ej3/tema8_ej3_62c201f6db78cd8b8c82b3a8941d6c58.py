import string

def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

def contar_caracteres(frase):
    return len(frase)

def largo_promedio_palabras(frase):
    palabras = frase.split()
    palabras_limpas = [palabra.strip(string.punctuation) for palabra in palabras]
    num_palabras = len(palabras_limpas)
    num_caracteres = sum(len(palabra) for palabra in palabras_limpas)
    if num_palabras > 0:
        return num_caracteres / num_palabras
    else:
        return 0

def contar_espacios(frase):
    return frase.count(' ')

def contar_caracteres_puntuacion(frase):
    caracteres_puntuacion = string.punctuation.replace(' ', '')
    return sum(frase.count(caracter) for caracter in caracteres_puntuacion)

def estadisticas_frase(frase):
    num_palabras = contar_palabras(frase)
    num_caracteres = contar_caracteres(frase)
    promedio_palabras = largo_promedio_palabras(frase)
    num_espacios = contar_espacios(frase)
    num_caracteres_puntuacion = contar_caracteres_puntuacion(frase)
    return num_palabras, num_caracteres, promedio_palabras, num_espacios, num_caracteres_puntuacion

if __name__ == "__main__":
    frase = '''El hombre imaginario
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
    circundado de cerros imaginarios...'''

    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])


         