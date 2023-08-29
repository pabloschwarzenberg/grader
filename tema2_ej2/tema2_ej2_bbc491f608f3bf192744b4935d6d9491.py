# completa el código de la función
def amigos(a, b):
    if a == b:
        return False

    sum_a = sum(divisores(a))
    sum_b = sum(divisores(b))

    return sum_a == b and sum_b == a

def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores