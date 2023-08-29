def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

def son_amigos(a, b):
    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False

# Ejemplo de uso:
num1 = 220
num2 = 284

if son_amigos(num1, num2):
    print("Los números", num1, "y", num2, "son amigos.")
else:
    print("Los números", num1, "y", num2, "no son amigos.")
