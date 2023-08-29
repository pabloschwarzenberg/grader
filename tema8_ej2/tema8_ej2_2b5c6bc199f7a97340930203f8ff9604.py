def buscarTodas(a,b):
    k = [i for i, string_b in enumerate(a) if string_b == b]

    j = list(k)

    lista = []

    for i in j:
        lista.append(str(i))

    espacio = " ".join(lista)

    return espacio
           