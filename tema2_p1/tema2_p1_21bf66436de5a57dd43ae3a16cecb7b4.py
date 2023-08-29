# por favor escribe aquí tu función
def es_primo(number):
    if number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True