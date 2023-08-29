def numeros_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)

    return suma_div_a == b and suma_div_b == a

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numeros_amigos(numero1, numero2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
