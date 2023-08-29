def buscarTodas(a,b):
    lista=[]
    i=0
    while i<len(a):
        x=a[i]
        if x ==b:
            lista.append(str(i))
        i = i+1
        d = " ".join(lista)
    return d   

           