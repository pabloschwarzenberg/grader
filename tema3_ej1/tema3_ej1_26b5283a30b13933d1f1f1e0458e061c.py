# completa el código de la función
def suma_divisores(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s==1:
        a=s,True
        return a
    else:
        b=s,False
        return b