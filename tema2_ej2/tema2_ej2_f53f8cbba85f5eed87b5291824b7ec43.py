# completa el código de la función
def amigos(a,b):
    valor=range(1,a)
    valor2=range(1,b)
    divisores=0
    for n in valor:
        if a % n == 0:
            divisores+=n
    print(divisores)
    div=0
    for i in valor2:
        if b % i == 0:
            div+=i
    print(div)
    if a == div and b == divisores:
        return True
    else:
        return False

           