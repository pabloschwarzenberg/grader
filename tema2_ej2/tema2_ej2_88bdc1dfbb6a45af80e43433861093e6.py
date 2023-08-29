# completa el código de la función
def amigos(a,b):
    suma = 0
    i = 0
    for i in range(1,a):
        if a%i == 0:
            suma = i+suma
    if suma == b:
        return True
    else:
        return False
    for i in range(1,b):
        if b%i == 0:
            suma = i+suma
    if suma == a:
        return True
    else:
        return False