def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    divisores_a = obtener_divisores(a)
    suma_divisores_a = sum(divisores_a)

    divisores_b = obtener_divisores(b)
    suma_divisores_b = sum(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if son_amigos(numero1, numero2):
    print("True")
else:
    print("False")
