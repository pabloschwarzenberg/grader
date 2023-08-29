# completa el código de la función
def suma_divisores(n):
    if n > 1:
        suma = 0
        for i in range(1,n):
            if n % i == 0:
                suma = suma + i
        if suma == 1:
            a = True
        else:
            a = False
        return (suma,a)
    else:
        return (0,False)