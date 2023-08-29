def suma_divisores(a):
    suma=0
    for i in range(1, a):
        if a %i==0:
            suma=suma+i
    if suma != 1:
        return suma,False
    else:
        return suma, True
print(suma_divisores(1))