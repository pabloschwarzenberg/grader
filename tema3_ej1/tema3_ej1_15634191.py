def suma_divisores(a):
    suma=0
    primo=False
    for i in range(1,a):
        if a%i==0:
            suma+=i
    if suma==1:
        primo=True
    return suma, primo

print(suma_divisores(6))