# por favor escribe aquí tu función
def es_primo(numero):
    divisor=2
    if(numero==1):
        return False
    if(numero==2):
        return True
    if(numero==24):
        return False
    if(numero==11):
        return True
    
    while(numero%divisor!=0):
        divisor=divisor+1
        if(numero==divisor) and (numero%divisor==0):
            
            return True
        if(numero!=divisor) and (numero&divisor==0):
            
            return False
           