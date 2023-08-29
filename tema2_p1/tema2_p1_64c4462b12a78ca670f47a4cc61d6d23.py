# por favor escribe aquí tu función
def es_primo(n):
    d = 2
    primo = True
    while n > d:
        if n % d == 0:
            primo = False
            break
        d += 1
    if primo and n > 1:
        return True
    else:
        return False