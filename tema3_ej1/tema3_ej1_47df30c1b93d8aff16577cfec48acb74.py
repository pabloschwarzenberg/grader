# completa el código de la función
def suma_divisores(a):
    divisores = [i for i in range(1,a+1) if a % i == 0]
    b = sum(divisores) - a
    if b == 1:
        return (b,True)
    else:
        return (b,False)


n = 13
print(suma_divisores(n))