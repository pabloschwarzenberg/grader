def buscarTodas(a,b):
    lista=[]
    lista2=[]
    espacio=" "
    contador=0
    for i in a:
        if i in a:
            lista2.append(i)
    while contador<len(a):
        if b is lista2[contador]:
            lista.append(str(contador))
        contador=contador+1
    return espacio.join(lista)