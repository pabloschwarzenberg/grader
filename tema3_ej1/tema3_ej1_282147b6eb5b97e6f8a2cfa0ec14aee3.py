def suma_divisores(a):
    suma=0
    cont=0
    flag = True
    for i in range(1,(a//2)+1):
        if a%i==0 :
            suma=suma+i
            cont=cont+1
    if cont==1:
        flag = True
    else:
        flag = False
    return (suma, flag)