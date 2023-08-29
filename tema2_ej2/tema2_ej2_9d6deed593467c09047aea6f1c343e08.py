# completa el código de la función
def amigos(a,b):
    suma_divisores_a = 0
    suma_divisores_b = 0
    for i in range(1,a):
        if a%i == 0:
            suma_divisores_a += i
    for j in range(1,b):
        if b%j == 0:
            suma_divisores_b += j
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False           