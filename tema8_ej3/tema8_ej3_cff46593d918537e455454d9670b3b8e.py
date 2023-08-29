def estadisticas_frase(frase):
    lista_espacio=frase.split(" ")
    contadorpuntuacion = 0
    for k in frase:
        if k == "." or k == ",":
            contadorpuntuacion = contadorpuntuacion + 1
    palabras=len(lista_espacio)
    espacios = palabras-1
    puntuacion = contadorpuntuacion
    palabras = espacios + 1
    caracteres = len(frase) - espacios - puntuacion
    largo = caracteres / palabras

    return (palabras, caracteres, largo, espacios, puntuacion)