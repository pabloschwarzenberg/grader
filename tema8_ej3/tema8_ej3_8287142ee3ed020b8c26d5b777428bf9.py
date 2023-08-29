def estadisticas_frase(s):
  if __name__ == "__main__":
    frase = """El hombre imaginario
     vive en una mansion imaginaria
     rodeada de arboles imaginarios
     a la orilla de un rio imaginario

     De los muros que son imaginarios
     penden antiguos cuadros imaginarios
     irreparables grietas imaginarias
     que representan hechos imaginarios
     ocurridos en mundos imaginarios
     en lugares y tiempos imaginarios
    
     Todas las tardes las tardes imaginarias
     sube las escaleras imaginarias
     y se asoma al balcon imaginario
     a mirar el paisaje imaginario
     que consiste en un valle imaginario..."""
    
    palabras = s.split()
    num_palabras = len(palabras)
    frasesinespacios = frase.replace(" ","")
    num_caracteres = len(frase)
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    num_espacios = s.count(" ")
    num_puntuacion = sum(1 for caracter in frase if not caracter.isalpha() and caracter == '.')

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])