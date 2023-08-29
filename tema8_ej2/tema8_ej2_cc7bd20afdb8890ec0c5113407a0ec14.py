def buscarTodas(a,b):
    posiciones_de_b = []
    lista_a = list(a)
    i = 0
    for letra in a:
        if letra == b:
            posiciones_de_b.append(str(a.find(b)+i))
            posiciones_de_b.append(" ")
        i += 1
    posiciones_de_b.pop(-1)
    posiciones = "".join(posiciones_de_b)

    return posiciones