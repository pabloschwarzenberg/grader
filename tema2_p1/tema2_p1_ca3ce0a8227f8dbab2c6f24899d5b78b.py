# por favor escribe aquí tu función
def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num, (11)):
            if num % i == 0:
                return False
        return True