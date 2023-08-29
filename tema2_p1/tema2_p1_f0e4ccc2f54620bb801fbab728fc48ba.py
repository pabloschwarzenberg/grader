# por favor escribe aquí tu función
def divisores(a):
    divisor = 1
    cantidad_divisores = 0
    while divisor <= a:
        if 0 == a%divisor:
            cantidad_divisores+=1
        divisor+=1
    return cantidad_divisores

def es_primo(n):
    if n == 1:
        return False
    elif divisores(n) <= 2:
        return True
    else:
        return False

k = int(input("Ingrese un número: "))

print(es_primo(k))