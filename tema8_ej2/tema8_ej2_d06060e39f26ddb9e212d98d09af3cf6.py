def buscarTodas(a,b):
    listaN = []
    for i in range(len(a)):
        if(a[i]==b):
            listaN.append(str(i))
        lista=" ".join(listaN)
        
    return lista

   