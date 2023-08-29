def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def amigos(a, b):
    suma_a = 0
    for i in range(1, a):
        if a % i == 0:
            suma_a += i
    suma_b = 0
    for i in range(1, b):
        if b % i == 0:
            suma_b += i
    if suma_a == b and suma_b == a:
        return True
    else:
        return False

# Ejemplo de uso de las funciones
r1 = es_primo(7)
r2 = amigos(1184, 1210)

print("¿Es primo 7? ", r1)
print("¿Son amigos 1184 y 1210? ", r2)