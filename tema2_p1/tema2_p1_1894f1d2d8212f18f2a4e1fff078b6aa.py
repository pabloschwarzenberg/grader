# por favor escribe aquí tu función
def es_primo(x):
    if x < 2:
        return False

    for num in range(2,x):
        if x%num == 0:
            return False

    return True
from random import randint
from time import sleep
