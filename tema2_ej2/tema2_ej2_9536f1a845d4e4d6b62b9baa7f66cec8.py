# completa el código de la función
def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if son_amigos(numero1, numero2):
    print(numero1, "y", numero2, "son números amigos")
else:
    print(numero1, "y", numero2, "no son números amigos")
