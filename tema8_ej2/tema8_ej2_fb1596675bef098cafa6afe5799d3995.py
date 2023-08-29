def buscarTodas(a,b):
    palabra = []
    inicio = 0
    final = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, inicio, final)
            palabra.append(str(pos))
            inicio = pos + 1
        except ValueError:
            break
    resultado= " ".join(palabra)

    return str(resultado)