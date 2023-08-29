# completa el código de la función
def calcular_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    sum_a = sum(calcular_divisores(a))
    sum_b = sum(calcular_divisores(b))

    return sum_a == b and sum_b == a

# Ejemplo de uso
resultado = son_amigos(220, 284)
print(resultado)