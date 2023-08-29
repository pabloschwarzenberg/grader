def numero_perfecto(a):
    i=1
    x=0
    suma=0
    while i<a:
        if a%i==0:
            suma=suma+i
        i=i+1
    if a==1:
        x=False
    if suma==a:
        x=True
    if suma!=a:
        x=False
    return x
a=6
numero_perfecto(a)
print(numero_perfecto(a))



           