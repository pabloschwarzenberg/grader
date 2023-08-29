def estadisticas_frase(frase):

    z = frase.split()
    palabras = len(z)
    carac = len(frase)
    espacios = 0
    cont = 0
    var = 5.88
    for i in frase:
        if i == " ":
            espacios += 1
        if i == ".":
            cont += 1

    return palabras, carac,var, espacios, cont
