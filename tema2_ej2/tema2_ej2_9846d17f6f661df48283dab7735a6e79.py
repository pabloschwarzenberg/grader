# completa el código de la función
def amigos(a,b):
    divisores_a = []
    divisores_b = []
    for i in range(1, a):   
        if a%i == 0:
            divisores_a.append(i)
    for d in range(1, b):
        if b%d == 0:
            divisores_b.append(d)
    suma_a = sum(divisores_a)
    suma_b =sum(divisores_b)
    if (suma_a == b) and (suma_b == a):
        return True
    else:
        return False
           