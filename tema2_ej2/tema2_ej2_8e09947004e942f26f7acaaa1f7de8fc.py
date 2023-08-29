# completa el código de la función
def amigos(a,b):
    n_a = 0
    n_b = 0
    for i in range(a):
        if a%(i+1) == 0:
            n_a += i+1
    for i in range(b):
        if b%(i+1) == 0:
            n_b += i+1

    if a != b and n_a == n_b:
        return True
    else:
        return False