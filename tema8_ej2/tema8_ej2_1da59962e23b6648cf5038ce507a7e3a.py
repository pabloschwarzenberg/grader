def buscarTodas(a,b):
    posicion=0
    lista=[]
    P2=""
    for i in a:
        if i==b:
            lista.append(posicion)
            posicion=posicion+1
        else:
            posicion=posicion+1
    for k in range(len(lista)):
        P2 = P2 + str(lista[k]) + " "
    P3=P2.rstrip()
    return P3
print(buscarTodas("tres tristes tigres","t"))