def suma_divisores(n):
    suma = sum(i for i in range(1,n) if n%i==0)
    if suma == 1:
        return suma, True
    else:
        return suma, False
           