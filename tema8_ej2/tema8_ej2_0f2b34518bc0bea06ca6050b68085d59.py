def buscarTodas(a,b):
    codigo = []
    for i in range (len(a)):
        letra = a[i]
        if letra == b:
            codigo.append(str(i))
    codigo = " ".join(codigo)
    return codigo