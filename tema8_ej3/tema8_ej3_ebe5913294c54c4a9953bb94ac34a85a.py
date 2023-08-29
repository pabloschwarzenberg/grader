def estadisticas_frase(s):
    n_caracteres = 0
    n_espacios = 0
    n_c_puntuacion = 0
    for letra in s:
        n_caracteres += 1
        if letra == ".":
            n_c_puntuacion += 1
        if letra == " ":
            n_espacios += 1
    s = s.split()
    suma = 0
    n_palabras = 0
    for palabra in s:
        n_palabras += 1
        suma += len(palabra)
    prom_largo = (suma - n_c_puntuacion) / n_palabras
    return n_palabras, n_caracteres, prom_largo, n_espacios, n_c_puntuacion