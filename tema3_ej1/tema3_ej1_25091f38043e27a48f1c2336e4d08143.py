# completa el código de la función

def suma_divisores(numero):
    divisores=0
    for i in range(1,(numero)):
        if numero%i==0:
            divisores=divisores+i
    if divisores==1:
        return divisores,True
    else:
        return divisores,False
            




           