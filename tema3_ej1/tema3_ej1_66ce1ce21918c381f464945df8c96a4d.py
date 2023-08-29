# completa el código de la función
def suma_divisores(n):
    divisores = []

    for i in range(1, n + 1):
        if n% i == 0:
            divisores.append(i)

    return sum(divisores)

resultado = suma_divisores(12)
print(resultado)
           