def son_amigos(a, b):
    def suma_divisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    return suma_a == b and suma_b == a
numero1 = int(input(" "))
numero2 = int(input(" "))
if son_amigos(numero1, numero2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")