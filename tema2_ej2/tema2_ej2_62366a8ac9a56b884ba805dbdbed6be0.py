# completa el código de la función
def amigos(a,b):
    suma_adivisores = 0
    suma_bdivisores = 0
    for i in range (1,a):
        if a % i == 0:
            suma_adivisores += i
    for c in range (1,b):
        if b % c == 0:
            suma_bdivisores += c
    if suma_adivisores == b and suma_bdivisores == a:
        return True
    else:
        return False