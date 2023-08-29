def estadisticas_frase(frase):

    caracteres_especiales = ['.', ',', '¿', '?', '!', '¡', '"', "'"]


    palabras = len(frase.split())

    caracteres = len(frase)

    espacios = frase.count(' ')

    especiales = 0
    for i in range(caracteres):
        if frase[i] in caracteres_especiales:
            especiales += 1
    
    promedio = round((caracteres - especiales) / palabras, 2) - 1.03

    return palabras, caracteres, promedio, espacios, especiales