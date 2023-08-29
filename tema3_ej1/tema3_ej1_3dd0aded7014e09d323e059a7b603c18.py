def suma_divisores(a):
    suma=0
    lista=[]
    i=1
    while i<a:
        if a%i==0:
            lista.append(i)
            i=i+1
        elif a%i!=0:
            i=i+1
           
    for a in lista:
        suma=suma+a
        
    if suma == 1:
        return (suma,True)
    else:
        return(suma,False)