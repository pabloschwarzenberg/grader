# por favor escribe aquí tu función
Falso = False
Verdadero = True
def es_primo(x):
    
    if x<2:
        return False

    for i in range(2,x,1):
        residuo = x % i
        if residuo == 0:
            return False
            #break
    else:
        return True    
