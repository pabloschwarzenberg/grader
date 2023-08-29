def estadisticas_frase(frase):
    caracteres = len(frase)
    num_espacios = 0
    num_puntuacion = 0

    for j in frase:
        if j == " ":
            num_espacios += 1
        if j == ".":
            num_puntuacion += 1

    frase = frase.strip(".")
    palabras = len(frase.split())

    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i += 1
        suma += sumatoria

    promedio = suma / palabras
    return palabras, caracteres, promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))