# completa el código de la función
def amigos(a,b):
    i = a-1
    sumaA = 0
    while i >= 1:
        if a%i == 0:
            sumaA += i
        i = i-1
    i = b-1
    sumaB = 0
    while i >= 1:
        if b%i == 0:
            sumaB += i
        i = i-1
    if a == sumaB and b == sumaA:
        return True
    else:
        return False
           