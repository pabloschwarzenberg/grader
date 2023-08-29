#def amigos(a,b):
def suma_divisores(num):

    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def amigos(a, b):

    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)
    
    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False
a = 220
b = 284

if amigos(a, b):
    print(a, "y", b," son números amigos")
else:
    print(a, "y", b, " no son números amigos")
