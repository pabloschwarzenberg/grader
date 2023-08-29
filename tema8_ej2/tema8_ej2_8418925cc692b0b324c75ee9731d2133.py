def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if a[i] == b:
            lista.append(str(i))
            
    pos=" ".join(lista) 
    return (pos)

