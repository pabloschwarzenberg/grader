def buscarTodas(a, b):
    i = 0
    lista = []
    lista.append(b)
    lista1 = []
    while i < len(a):
        if a[i] in lista:
            lista1.append(str(i))
            i += 1
        else:
            i += 1
    n = ""
    for l in lista1:
        n += l + " "
    n = n.strip()
    
    return n
    

           