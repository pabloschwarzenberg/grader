def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        caracter=a[i]
        if caracter==b:
            lista.append(str(i))
    return ' '.join(lista)