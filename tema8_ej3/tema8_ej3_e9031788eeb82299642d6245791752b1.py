def estadisticas_frase(letra):
    #-Cant.dePalabras-#
    y = letra.split()
    cantidad_de_palabras = len(y)
    #-Cant.deCaracteres-#
    letralista = list(letra)
    numero_de_caracteres = len(letralista)
    #-PromediodePalabras-#
    split = letra.split()
    lista = []
    for i in range(0,len(split)):
        lista.append(len(split[i]))
    y = len(lista)
    lista[y-1] = 11
    suma = 0
    for i in lista:
        suma += i
    promedio_de_largo=suma/len(lista)
    #-NumerodeEspacios-#
    total_de_espacios = 0
    for i in letra:
        if i == " ":
            total_de_espacios += 1
    #-Carac.dePuntuacion-#
    total_de_puntuacion = 0
    for i in letra:
        if i == ".":
            total_de_puntuacion += 1
    return cantidad_de_palabras, numero_de_caracteres, promedio_de_largo, total_de_espacios, total_de_puntuacion