# completa el código de la función
def amigos(a, b):
    suma__a = sum(divisores(a))
    suma__b = sum(divisores(b))
    
    if suma__a == b and suma__b == a:
        return True
    else:
        return False

def divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores
           