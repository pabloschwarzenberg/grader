# por favor escribe aquí tu función
def es_primo(x):
    if x < 2:
        return False
    else:
        for i in range(2, x+1):
            if x == i:
                return True
            elif x % i == 0:
                return False