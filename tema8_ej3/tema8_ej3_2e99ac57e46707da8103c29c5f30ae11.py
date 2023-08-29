def estadisticas_frase(frase):
    caracteres = len(frase)
    n_espacios  = 0
    n_puntiacion = 0
    i = " "
    for i in frase:
        if i == " ":
            n_espacios = n_espacios + 1
        if i == ".":
            n_puntiacion = n_puntiacion +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    
    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0 
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i = i + 1
        suma = suma + sumatoria
    promedio = suma/palabras
    return palabras, caracteres, promedio, n_espacios, n_puntiacion
         