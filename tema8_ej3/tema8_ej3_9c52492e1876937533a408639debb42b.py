def estadisticas_frase(frase):
    caracteres = len(frase)
    num_espacios  = 0
    num_puntiacion = 0
    j = " "
    for j in frase:
        if j == " ":
            num_espacios = num_espacios + 1
        if j == ".":
            num_puntiacion = num_puntiacion +1
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
    return palabras, caracteres, promedio, num_espacios, num_puntiacion  