def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if son_amigos(numero1, numero2):
    print("Los números son amigos")
else:
    print("Los números no son amigos")
           