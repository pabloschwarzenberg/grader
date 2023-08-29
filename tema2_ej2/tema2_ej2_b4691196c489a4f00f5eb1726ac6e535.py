def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

# Solicitar al usuario ingresar los números
numero_a = int(input("Ingrese el primer número: "))
numero_b = int(input("Ingrese el segundo número: "))

# Verificar si los números son amigos
if son_amigos(numero_a, numero_b):
    print("¡Los números son amigos!")
else:
    print("Los números no son amigos.")
