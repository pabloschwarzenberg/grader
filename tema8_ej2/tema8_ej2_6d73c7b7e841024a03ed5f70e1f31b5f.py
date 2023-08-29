def buscarTodas(a,b):
    if b in a:
        posicion=[]
        for i in range(0,len(a)):
            if a[i]==b:
               posicion.append(str(i))
    posicion=" ".join(posicion)
    return posicion        