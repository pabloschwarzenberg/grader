def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if b==a[i]:
            lista.append(i)
            string=" ".join(str(e) for e in lista)

    return string  