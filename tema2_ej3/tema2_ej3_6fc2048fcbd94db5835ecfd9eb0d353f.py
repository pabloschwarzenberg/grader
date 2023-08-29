def numero_perfecto(a):
    num=a
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma=suma+i
    if suma==num:
        resultado=True
    else:
        resultado=False
    return resultado
           