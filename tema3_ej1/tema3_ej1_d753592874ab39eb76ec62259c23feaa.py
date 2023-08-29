# completa el código de la función

def suma_divisores(numero):
    divisor=1
    suma=0
    suma2=0
    while divisor<numero:
        if numero%divisor==0:
            suma+=1
            suma2+=divisor
            divisor+=1
        else:
            divisor+=1
    if suma==1:
        return (suma2,True)
    else:
        return (suma2,False)
           