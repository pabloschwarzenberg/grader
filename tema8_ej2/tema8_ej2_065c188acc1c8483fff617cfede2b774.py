def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if a[i:i+len(b)]==b:
            lista.append(str(i))
    return " ".join(lista)