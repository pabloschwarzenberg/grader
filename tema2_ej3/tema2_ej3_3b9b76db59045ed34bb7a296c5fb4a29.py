def numero_perfecto(a):
    suma = 0
    lista=[]
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
            lista.append(i)
    if suma == a:
        return True
    else:
        return False
        