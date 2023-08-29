# por favor escribe aquí tu función
def es_primo(n):
    a = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            a = a + 1
    if (a != 2):
        return False
    else:
        return True
    return         