def es_primo(x):
    "Se  dice que ningun número mayor que 2 es primo"    
    if x<2:
        return False

    for i in range(2,x,1):
        resto = x % i
        if resto == 0:
            return False
    else:
        return True    