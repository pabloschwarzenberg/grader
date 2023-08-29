# completa el código de la función
def amigos(a,b):
    aa = 0
    ab = 0
    for i in range(1, a+1):
        if a%i == 0 and i != a:
            aa += i
    for i in range(1, b+1):
        if b%i == 0 and i != b:
            ab += i
    if aa == b and ab == a:
        return True
    else:
        return False