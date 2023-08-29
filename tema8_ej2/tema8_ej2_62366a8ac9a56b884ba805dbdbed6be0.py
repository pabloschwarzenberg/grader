def buscarTodas(a,b):
    apariciones = []
    for x in range(0, len(a)-1):
        if a[x] == b:
            apariciones.append(str(x))
    apariciones = " ".join(apariciones)
    return apariciones