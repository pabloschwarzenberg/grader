import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    
    # Calcular el largo promedio de las palabras
    palabras_validas = [palabra.strip(string.punctuation) for palabra in palabras]
    largo_promedio = sum(len(palabra) for palabra in palabras_validas) / len(palabras_validas)

    num_espacios = s.count(' ')
    num_puntuacion = sum(1 for caracter in s if caracter in string.punctuation and caracter != ' ')
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    frase = """El hombre imaginario
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

    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])