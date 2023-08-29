# completa el código de la función
def suma_divisores(a):
    n=0

    for i in range(1,a):
        if a % i == 0:
            n += i

    if n == 1:
        print("es primo")
        return n,True
    else:
        return n,False