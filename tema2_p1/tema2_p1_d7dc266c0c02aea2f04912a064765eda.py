# por favor escribe aquí tu función
def es_primo(numero):
    divisor=0
    for i in range(1, numero+1):
        if (numero%i)==0:
            divisor +=1
    
    if numero > 1 and divisor==2:
        return True
    else:
        return False