# por favor escribe aquí tu función
def es_primo(numero):
    divisores=0
    if numero< 2:    
        return False
    else:
        for x in range(2, numero): 
            if numero%x == 0:    
                divisores=divisores+1
                
        if divisores>0:
            return False   
        else:
            return True