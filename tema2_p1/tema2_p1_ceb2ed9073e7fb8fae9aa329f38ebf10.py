# por favor escribe aquí tu función
def es_primo(n):
    for n1 in range(1, n):
        if n % n1 == 0 :
            return True
    return False