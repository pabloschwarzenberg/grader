def buscarTodas(a,b):
    contador=0
    lista=[]
    for i in a:
        if i == b:
            lista.append(str(contador))
        contador=contador+1

    resultado = " ".join(lista)
    return resultado
