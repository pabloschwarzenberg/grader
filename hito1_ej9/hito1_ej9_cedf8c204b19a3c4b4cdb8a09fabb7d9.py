#Sistema de Ecuaciones
def divisores(x):
    numero = []
    for i in range (1, x):
        if x % i == 0:
           numero.append(i)
    return sum(numero)
    
def amigos(a,b):
    if divisores(a) == b and divisores(b) == a:
        return True
    else:
        return False      