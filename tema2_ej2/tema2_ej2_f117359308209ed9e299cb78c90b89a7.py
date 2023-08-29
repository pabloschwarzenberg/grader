def amigos(num1, num2):
    def sum_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    return sum_divisores(num1) == num2 and sum_divisores(num2) == num1

# Ejemplo de uso
print(amigos(220, 284))  # True
print(amigos(1184, 1210))  # True
print(amigos(220, 221))  # False