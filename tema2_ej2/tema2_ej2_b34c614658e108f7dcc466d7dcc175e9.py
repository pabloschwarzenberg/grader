# completa el código de la función
def divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

def amigos(a, b):
    suma_divisores_a = divisores(a)
    suma_divisores_b = divisores(b)
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplo de uso de la función
numero1 = 220
numero2 = 284
r1 = amigos(numero1, numero2)
if r1:
    print("Los números", numero1, "y", numero2, "son amigos.")
else:
    print("Los números", numero1, "y", numero2, "no son amigos.")
           