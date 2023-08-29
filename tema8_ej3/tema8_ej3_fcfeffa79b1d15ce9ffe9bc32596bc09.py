def estadisticas_frase(frase):
    lista_palabras = frase.split()
    numero_palabras = len(lista_palabras)
    numero_caracteres = len(frase)
    numero_espacios = 0
    promedio = []
    numero_especiales = 0
    for index in lista_palabras:
        if index == "imaginarios...":
            promedio.append(len(index) - 3)
            for j in index:
                if j == ".":
                    numero_especiales += 1
        else:
            promedio.append(len(index))
    promedio_letras = sum(promedio) / numero_palabras
    print(promedio_letras)

    for index in frase:
        if " " in index:
            numero_espacios += 1
    mensaje = (numero_palabras, numero_caracteres, promedio_letras, numero_espacios, numero_especiales)
    return mensaje
