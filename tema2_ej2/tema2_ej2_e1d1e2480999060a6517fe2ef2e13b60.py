def suma(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores

def amigos(a, b):
    suma_a = suma(a)
    suma_b = suma(b)
    return suma_a == b and suma_b == a

n1 = 220
n2 = 284

if amigos(n1, n2):
    print("True")
else:
    print("False")
