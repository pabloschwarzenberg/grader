# completa el código de la función
def suma_divisosres(n):
    sumador=0
    for i in range (1,n,1):
        e=n%i
        if e == 0:
            sumador+=i
    return (sumador)