# completa el código de la función
def son_amigos(a, b):
    def calcular_suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = calcular_suma_divisores(a)
    suma_b = calcular_suma_divisores(b)

    return suma_a == b and suma_b == a

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if son_amigos(num1, num2):
        print(True)
    else:
        print(False)