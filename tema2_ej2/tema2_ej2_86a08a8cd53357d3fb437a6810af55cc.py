# completa el código de la función
def amigos(a,b):
    k = 0
    m = 0
    for numero in range(1,a):
        if a % numero == 0:
            k += numero
    for numero in range(1,b):
        if b % numero == 0:
            m += numero

    if k == b and m == a:
        return True
    else:
        return False
           