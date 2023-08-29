# completa el código de la función
def amigos(a,b):
    suma_a=1
    suma_b=1
    inicio_a=2
    inicio_b=2
    for i in range(inicio_a,a-1):
        if a%inicio_a==0:
            suma_a=suma_a+inicio_a
            inicio_a=inicio_a+1
        else:
            inicio_a=inicio_a+1
    for i in range(inicio_b,b-1):
        if b%inicio_b==0:
            suma_b=suma_b+inicio_b 
            inicio_b=inicio_b+1
        else:
            inicio_b=inicio_b+1
    if suma_a==b and suma_b==a:
        return True
    else:
        return False           