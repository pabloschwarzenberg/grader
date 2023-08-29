def buscarTodas(a,b):
    i=0
    T=[]
    while i<len(a):
        if a[i]==b:
            T.append(i)
        i=i+1
        
    cadena = ' '.join([str(x) for x in T])
    return cadena