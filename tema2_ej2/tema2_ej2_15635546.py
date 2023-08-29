# completa el código de la función

# completa el código de la función

def amigos(a,b):
    suma_a = 0
    suma_b = 0
    amigos = False
    for i in range (1,a):
        if a % i == 0:
            suma_a = suma_a + i
    for n in range (1, b):
        if b % n == 0:
            suma_b = suma_b + n
    if suma_a == b and suma_b == a:
        amigos = True

    return amigos