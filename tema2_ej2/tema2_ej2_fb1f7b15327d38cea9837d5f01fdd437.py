from os import system
system("cls")


def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
            return divisores

def son_amigos(numero1, numero2):
    divisores_numero1 = calcular_divisores(numero1)
    suma_divisores_numero1 = sum(divisores_numero1)
    divisores_numero2 = calcular_divisores(numero2)
    suma_divisores_numero2 = sum(divisores_numero2)
    return suma_divisores_numero1 == numero2 and suma_divisores_numero2 == numero1

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
if son_amigos(numero1, numero2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")