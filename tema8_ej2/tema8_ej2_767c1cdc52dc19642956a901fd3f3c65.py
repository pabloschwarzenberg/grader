def buscarTodas(a,b):
    posicion=[]
    final=""
    for i in range(0,len(a)):
        if a[i]==b:
            posicion.append(i)
    for i in range(0,len(posicion)):
        final=final+" "+str(posicion[i])
    return final.strip()
    