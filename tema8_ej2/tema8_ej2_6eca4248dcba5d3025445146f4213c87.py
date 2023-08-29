def buscarTodas(a,b):
    lista1=[]
    lista2=[]
    i=0
    while i<len(a):
        lista1.append(a[i])
        if a[i]==b:
            lista2.append(i)
        i=i+1
    
   
    return " ".join([str(lista2[0]),str(lista2[1]),str(lista2[2]),str(lista2[3])])