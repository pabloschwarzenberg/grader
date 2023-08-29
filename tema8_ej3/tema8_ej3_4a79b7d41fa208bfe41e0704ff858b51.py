def estadisticas_frase(s):

    # retorne el número de palabras, el número total de caracteres, el largo promedio de las palabras,
    # el número de espacios, y el número de caracteres de puntuación (que no sean letras o espacios).

    # primer paso, encontrar el numero total de caracteres
    total_caracteres = len(list(s))

    # segundo paso, encontrar numero de palabras
    total_palabras = len(s.split())

    # tercer paso, encontrar el largo promedio de las palabras (sin puntuacion), el numero de espacios,
    # ...el numero de caracteres de puntuacion que no sean letras o espacio
    caracter_alpha = 0
    caracter_espacio = 0
    caracter_puntuacion = 0

    # iterar caracter a caracter
    for i in range(len(s)):

        if s[i].isalpha():
            caracter_alpha += 1
        elif s[i] == " ":
            caracter_espacio += 1
        else:
            caracter_puntuacion += 1

    largopromedio = caracter_alpha / total_palabras
    
    return total_palabras, total_caracteres, largopromedio, caracter_espacio, caracter_puntuacion
