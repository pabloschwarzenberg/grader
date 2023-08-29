def son_amigos(a, b):
    sum_div_a = sum(divisores(a))
    sum_div_b = sum(divisores(b))

    return sum_div_a == b and sum_div_b == a


def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores


# Ejemplo de uso
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if son_amigos(num1, num2):
    print("Los números", num1, "y", num2, "son amigos.")
else:
    print("Los números", num1, "y", num2, "no son amigos.")
