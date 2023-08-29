# por favor escribe aquí tu función
def es_primo(numero):
    divisor=2
    while divisor<numero:
        n=numero%divisor
        if n==0:
            divisor=numero
        divisor=divisor+1
    if divisor==numero+1:
        return False
    else:
        return True
  
 
           