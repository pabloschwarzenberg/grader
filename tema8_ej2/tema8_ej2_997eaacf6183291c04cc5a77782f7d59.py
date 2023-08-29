def buscarTodas(a,b):
    L = []
    for i in range(len(a)):
        if a[i] == b:
            L.append(i)
    L = list(map(str,L))
    respuesta = " ".join(L)    
    return respuesta

           