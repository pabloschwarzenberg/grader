def suma_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % 1 == 0]

    return sum(divisores)

resultado = suma_divisores(3)
print(resultado)