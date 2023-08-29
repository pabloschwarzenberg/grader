# completa el código de la función
def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    divisores_a = obtener_divisores(a)
    suma_divisores_a = sum(divisores_a)

    divisores_b = obtener_divisores(b)
    suma_divisores_b = sum(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if son_amigos(n1, n2):
    print(n1, "y", n2, "son amigos.")
else:
    print(n1, "y", n2, "no son amigos.")