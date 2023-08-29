# por favor escribe aquí tu función
def es_primo(numero):
    divisor=2
    esprimo=True
    if numero==1:
        esprimo=False
    while esprimo and divisor<=numero/2:
        if numero%divisor==0:
            esprimo=False
        divisor+=1
    if esprimo==True:
        return True
    else:
        return False
           