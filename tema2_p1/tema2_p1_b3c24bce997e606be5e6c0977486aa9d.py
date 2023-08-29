# por favor escribe aquí tu función
def es_primo(a):
    if a > 1:
        for i in range(2,a):
            if a % i == 0:
                return False
            return True
    else:
        return False
           