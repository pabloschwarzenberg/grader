def son_amigos(a, b):
    def obtener_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if son_amigos(num1, num2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
           