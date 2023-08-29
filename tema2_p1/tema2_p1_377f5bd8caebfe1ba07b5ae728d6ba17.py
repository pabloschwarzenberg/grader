# por favor escribe aquí tu función
def es_primo(num):
    f = True
    if num == 2 or num == 3:
        f = True
    elif num == 1:
        f = False
    elif num%2 == 0:
        f = False
    elif num%3 == 0:
        f = False
    return f