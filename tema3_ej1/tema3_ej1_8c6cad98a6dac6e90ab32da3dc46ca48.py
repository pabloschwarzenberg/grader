def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            if i!=numero:
                suma += i
    a=False
    if suma==1:
        a=True
    return suma,a

