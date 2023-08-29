def son_amigos(a, b):
    def sum_divisores(num):
        return sum(i for i in range(1, num) if num % i == 0)

    suma_divisores_a = sum_divisores(a)
    suma_divisores_b = sum_divisores(b)

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplo de uso
num1 = 220
num2 = 284

if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos")
else:
    print(f"{num1} y {num2} no son números amigos")
