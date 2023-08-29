# por favor escribe aquí tu función

def es_primo(x):
    verif = 0
    if x < 2:
        return False

    for num in range(2,x):
        if x%num == 0: 
            verif = verif + 1
            
    if verif > 1:      
       return False

    return True