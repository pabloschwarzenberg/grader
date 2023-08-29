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

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
numero_a = int(input("Ingrese el número a: "))
numero_b = int(input("Ingrese el número b: "))

if son_amigos(numero_a, numero_b):
    print("Los números son amigos")
else:
    print("Los números no son amigos")