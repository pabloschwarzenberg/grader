# por favor escribe aquí tu función
def es_primo(n):    
    if n< 2: 
        return False
    for i in range(2, n):
        if n% i == 0:
            return False 
    return True