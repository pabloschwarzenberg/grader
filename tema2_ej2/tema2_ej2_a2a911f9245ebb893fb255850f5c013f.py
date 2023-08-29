def divisores(x):
    numeros= []
    for i in range (1, x):
        if x % i == 0:
            numeros.append(i)
    return sum(numeros)
    
def amigos(a,b):
    if divisores(a) == b and divisores(b) == a: 
        return True
    else:
        return False