# por favor escribe aquí tu función
Falso = False
Verdadero = True
num= 2
def es_primo(x):
    """ El Hint dice ningun número
        mayor que 2 es primo    """    
    if x<2:
        return False

    for i in range(2,x,1):
        residuo = x % i
        if residuo == 0:
            return False
            #break
    else:
        return True    
print(es_primo(num))