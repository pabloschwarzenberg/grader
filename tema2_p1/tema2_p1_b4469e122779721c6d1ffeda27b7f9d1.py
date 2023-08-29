#numero Primo
def es_primo(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for w in range(2, x):
            if x % w == 0:
              return False
        return True
