def estadisticas_frase(frase):
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = frase.count(" ")
    caracteres_puntuacion = sum(1 for caracter in frase if not caracter.isalnum() and caracter != " ")

    return num_palabras, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion

if __name__ == "__main__":
  
    resultado = estadisticas_frase(hombre_imaginario)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
