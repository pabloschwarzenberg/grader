import random

def encriptar():
    x = random.randrange(1,11)
    b = random.randrange(1,11)
    c = random.randrange(1,11)
    c = str(c)
    b = str(b)
    x = str(x)
    resultado = x + b + c
    return (resultado)

