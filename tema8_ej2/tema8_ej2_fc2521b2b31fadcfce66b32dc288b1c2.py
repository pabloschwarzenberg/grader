def buscarTodas(a,b):
    contador=0
    lista=[]
    for s in a:
        if s == b:
            lista.append(str(contador))
        contador=contador+1

    resultado = " ".join(lista)
    return resultado
           