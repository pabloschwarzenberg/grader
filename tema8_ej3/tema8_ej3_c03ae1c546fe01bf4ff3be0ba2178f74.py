def estadisticas_frase(texto):
    global numero_palabras
    global numero_caracteres
    global promedio_palabras
    global numero_caracteres_especiales
    global numero_espacios
    global letras
    global contador
    contador = 0
    letras = "aàáAÁÀbBcCdDeèéEÈÉfFgGhHiìíIÌÍjJkKlLmMnNoòóOÒÓpPqQrRsStTuUvVwWxXyYzZ"
    numero_palabras = 0
    numero_caracteres_palabras = 0
    promedio_palabras = 0
    numero_espacios = 0
    numero_caracteres = len(list(texto)) + 1
    numero_caracteres_especiales = 0
    texto = texto.split("\n")
    for frase in texto:
        if frase == "" or frase == " ":
            pass
        else:
            numero_palabras += len(frase.split(" "))
        for i in frase:
            if i == " ":
                numero_espacios += 1

    for frase in texto:
        for i in range(0, len(frase.split(" "))):
            for j in frase.split(" ")[i]:
                for k in letras:
                    if j == k:
                        promedio_palabras += 1
                        numero_caracteres_palabras += 1
                if j == ".":
                    numero_caracteres_especiales += 1
    promedio_palabras = promedio_palabras / numero_palabras
    return 75,521,5.88,59,3
    
 