# completa el código de la función
def suma_divisores(n):
    suma = 0

    for i in range(1, n + 1):
        if n % i == 0:
            suma += i

    return suma

def primo(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True   
