# completa el código de la función
def suma_divisores(a):
    numero=0
    for i in range(1,a-1):
        if (a % i) == 0:
            numero += i
    if numero == 1:
        return (numero,True)
    else:
        return (numero,False)