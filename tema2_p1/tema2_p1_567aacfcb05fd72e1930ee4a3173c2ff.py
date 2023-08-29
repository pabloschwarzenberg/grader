# por favor escribe aquí tu función
def es_primo(n):
    if n == 1:
        return False
    elif n ==2:
        return True
    else:
        for j in range(2, n):
            if n % j == 0:
                return False
        return True