# por favor escribe aquí tu función
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        return True
    if num == 1:
        return False