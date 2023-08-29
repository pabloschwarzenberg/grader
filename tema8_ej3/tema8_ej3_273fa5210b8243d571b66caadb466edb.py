def estadisticas_frase(s):
    s = s.remove('\n')
    promedio = []
    p = 0
    espacios = 0
    puntuacion = 0
    signos_de_puntuacion = '.,:;¡!¿?()"-_'
    lista_de_palabras = s.split(' ')
    for palabra in lista_de_palabras:
        largo = len(palabra)
        promedio.append(largo)
    for numero in promedio:
        p += numero
    for caracter in s:
        if caracter == ' ':
            espacios += 1
        elif caracter in signos_de_puntuacion:
            puntuacion += 1
    promedio_largo_palabra = p/len(promedio)
    cantidad_palabras = len(lista_de_palabras)
    caracteres = len(s)
    return cantidad_palabras, caracteres, promedio_largo_palabra, espacios, puntuacion

