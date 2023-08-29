def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if a[i]==b:
            lista.append(str(i))
    
    imprime=" ".join(lista)
    
    return imprime

           