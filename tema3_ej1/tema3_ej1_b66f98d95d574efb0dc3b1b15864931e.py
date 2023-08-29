def suma_divisores(n):
    divisores = [1]

    for i in range(2, n + 1):
        if n % i == 0:
            divisores.append(i)

    return sum(divisores)

resultado = suma_divisores(10)
print(resultado)
