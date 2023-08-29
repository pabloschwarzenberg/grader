# por favor escribe aquí tu función
def es_primo(n):
    x = 1
    y = 0
    while n >= x:
        if (n % x) == 0:
            y += 1
        x += 1
    if y == 2:
        return True
    else:
        return False