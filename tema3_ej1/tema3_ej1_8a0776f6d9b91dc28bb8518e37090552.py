# completa el código de la función
numero = 8
def suma_divisores(a):
    sum = 0
    n=1
    while (n < a):
        if a % n == 0:
            sum=sum+n
        n = n+1
    if sum == 1:
        primo = 1
    else:
        primo = 0
    return sum,primo

su,pri = suma_divisores(numero)
           