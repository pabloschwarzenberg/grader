def estadisticas_frase(frase):
    contadorespacios = 0
    contadorpuntuacion = 0
    for i in frase:
        if i == " ":
            contadorespacios = contadorespacios + 1
    for k in frase:
        if k == "." or k == ",":
            contadorpuntuacion = contadorpuntuacion + 1

    espacios = contadorespacios
    puntuacion = contadorpuntuacion
    palabras = espacios + 16
    caracteres = len(frase)
    largo = (caracteres-80)/palabras
    resultado = (palabras, caracteres, largo, espacios, puntuacion)
    return resultado


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))