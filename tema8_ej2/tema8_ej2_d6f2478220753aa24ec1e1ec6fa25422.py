def buscarTodas(a,b):
    letras = []
    for i in range(len(a)):
        if a[i] == b:
            letras.append(i)
    if len(letras) == 0:
        return "no existe"

    return letras