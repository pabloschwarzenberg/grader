def buscarTodas(a,b):
    lista=[]
    n=0
    while n<len(a):
        if a[n]==b:
            lista.append(str(n))
        n+=1
    listaa=" ".join(lista)
    return listaa
   

           