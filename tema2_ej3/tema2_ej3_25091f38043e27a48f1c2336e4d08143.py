def numero_perfecto(numero):
    divisores=0
    for i in range(1,(numero)):
        if numero%i==0:
            divisores=divisores+i
    if numero==divisores:
        return True
    else:
        return False
           