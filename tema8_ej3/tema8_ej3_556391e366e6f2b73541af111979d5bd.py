def estadisticas_frase(frase):
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = sum(caracter == ' ' for caracter in frase)
    caracteres_puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    num_caracteres_puntuacion = sum(caracter in caracteres_puntuacion for caracter in frase)

    return f"{num_palabras}, {num_caracteres}, {largo_promedio:.2f}, {num_espacios}, {num_caracteres_puntuacion}"

