def es_primo(numero):
    divisor=2
    if numero==1 or numero==0:
        return False
    elif numero==2:
        return True
    while divisor<numero:
        if numero%divisor==0:
             return False
        divisor+=1
    return True
 

     
           