# completa el código de la función
def amigos(a,b):
    sumaa = 0
    sumab = 0
    for i in range(1,a):
        if a % i == 0:
            sumaa += i

    for k in range(1,b):
        if b % k == 0:
            sumab += k

    if sumaa == b and sumab == a:
        return True
    else:
        return False