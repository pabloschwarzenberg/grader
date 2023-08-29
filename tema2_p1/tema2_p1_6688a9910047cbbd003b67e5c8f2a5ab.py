# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
        return False
    if numero==2:
        return True
        
    if numero==3:
        return True
        
    else:
        divisor=2
        while divisor<numero:
            if numero%divisor==0:
                return False
            else:
                divisor=divisor+1
            if divisor==numero-1:
                return True
 