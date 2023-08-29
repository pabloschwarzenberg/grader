def buscarTodas(a,b):
    contar = len(a)
    palabra= list(a)
    lista=[]
    posicion=0
    for x in range(0,contar):
        if palabra[x]==b:
            lista.insert(posicion,x)
                               
            lista.insert(posicion+1," ")
            
            posicion +=2
        if x == contar-1:
            lista.pop(-1)
    y=''.join(str(x)for x in lista)
    
    return y