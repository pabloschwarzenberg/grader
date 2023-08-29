def buscarTodas(a,b):
    pos = "" # acumulador
    for i in range(len(a)):
        if b==a[i]:
            pos = pos + str(i) + " "
    pos = pos.rstrip(" ")
    return pos