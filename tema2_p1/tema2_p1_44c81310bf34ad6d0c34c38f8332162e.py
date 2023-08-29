# por favor escribe aquí tu función
def es_primo(x):
    divisor = 0
    for w in range(1, x+1):
        if x % w == 0:
            divisor += 1
    if divisor == 2:
        return True
    else:
        return False
print(es_primo(23))

