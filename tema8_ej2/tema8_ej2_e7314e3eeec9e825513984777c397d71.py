def buscarTodas(a,b):
    posiciones=[]
    i=0
    largo=len(a)
    for i in range(largo) :
        if a[i]==b:
            posiciones.append(str(i))
    final=" ".join(posiciones)
    return final
