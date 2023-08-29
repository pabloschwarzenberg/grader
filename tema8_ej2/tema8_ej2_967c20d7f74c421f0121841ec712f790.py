def buscarTodas(a,b):
    cadena = []
    for i in range(len(a)):
        if a[i] == b:
            cadena.append(i)
    StrA = " ".join([str(_) for _ in cadena])
    return StrA