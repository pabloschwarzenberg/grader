def suma_divisores(a):
    #recibimos como parametro solo el numero a, al cual queremos obtener sus divisores
    divisor=1
    divisores=[]
    while divisor<a :
        resto=a%divisor
        if resto==0 :
            divisores.append(divisor)
        divisor=divisor+1
    suma=0
    for i in divisores:
        suma=suma+i
    print(suma)
    if len(divisores)==1:
        return(suma,True)
    else:
        return(suma,False)