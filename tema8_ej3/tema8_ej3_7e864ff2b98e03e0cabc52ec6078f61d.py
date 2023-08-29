def estadisticas_frase(frase):
    numerocaracteres = len(frase)
    split = frase.split()
    numeroespacios = 0
    numeropuntuacion = 0
    numeropalabras = len(split)
    for i in frase:
        if i == " ":
            numeroespacios += 1

    for i in frase:
        if i == ".":
            numeropuntuacion += 1

    numeroletras=0
    nuevaFrase = frase.strip(".")
    nuevafraseLista = nuevaFrase.split()
    for palabra in nuevafraseLista:
        numeroletras += len(palabra)


    largopromedio = float(numeroletras) / float (numeropalabras)

    return numeropalabras, numerocaracteres, largopromedio, numeroespacios, numeropuntuacion