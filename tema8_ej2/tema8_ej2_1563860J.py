def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if a[i]==b:
            lista.append(i)
    str1 = " ".join(str(x) for x in lista)        
    return str1     