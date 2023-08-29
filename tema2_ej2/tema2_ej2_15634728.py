# completa el código de la función
def d(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    return suma

def amigos(a,b):
    if d(a) == b and d(b) == a and a != b:
        return True
    else:
        return False           