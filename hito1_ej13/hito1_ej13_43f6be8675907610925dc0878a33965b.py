#Factores Primos
def divisores(n):
    divisor=1
    cantidad_divisores=0
    while divisor<=n:
        if n%divisor==0:
            cantidad_divisores=cantidad_divisores+1
        divisor=divisor+1
    return cantidad_divisores

def es_primo(n):
    if divisores (n)==2:
        return True
    else:
        return False
