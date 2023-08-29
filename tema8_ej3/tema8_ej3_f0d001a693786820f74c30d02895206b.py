import string

def estadisticas_frase(s):
   
    for c in string.punctuation:
        s = s.replace(c, " ")

  
    palabras = s.split()

    
    num_palabras = len(palabras)

   
    num_caracteres = len(s)


    sum_len_palabras = sum(len(p) for p in palabras)
    largo_prom_palabras = sum_len_palabras / num_palabras

    
    num_espacios = s.count(" ")

    
    num_puntuacion = len(s) - len(s.translate(str.maketrans("", "", string.punctuation)))

    
    return (num_palabras, num_caracteres, largo_prom_palabras, num_espacios, num_puntuacion)

if __name__ == "__main__":
    poema = """El hombre imaginario
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

    resultados = estadisticas_frase(poema)
    print("Número de palabras:", resultados[0])
    print("Número total de caracteres:", resultados[1])
    print("Largo promedio de las palabras:", resultados[2])
    print("Número de espacios:", resultados[3])
    print("Número de caracteres de puntuación:", resultados[4])
         