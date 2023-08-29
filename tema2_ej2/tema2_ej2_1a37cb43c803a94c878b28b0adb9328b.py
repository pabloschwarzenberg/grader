# completa el código de la función
def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    divisores_a = calcular_divisores(a)
    suma_divisores_a = sum(divisores_a)

    divisores_b = calcular_divisores(b)
    suma_divisores_b = sum(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
num1 = 220
num2 = 284

if son_amigos(num1, num2):
    print("Los números son amigos")
else:
    print("Los números no son amigos")