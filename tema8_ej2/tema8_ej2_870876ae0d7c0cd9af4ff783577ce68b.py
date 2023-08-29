def buscarTodas(a,b):
    apariciones = []
    c = list(a)
    i = 0
    while i < len(a):
        if a[i] == b:
            apariciones.append(str(c.index(a[i],i)))
        i = i+1
    return ' '.join(apariciones)