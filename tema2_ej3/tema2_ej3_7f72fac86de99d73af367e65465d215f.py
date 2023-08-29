def numero_perfecto(a):
    divisor=2
    suma=0
    while divisor < a :
            if a%divisor==0:  
                numero=a//divisor
                suma=suma+numero
            divisor += 1
    suma+=1
    if suma==a:
        return True
    else:
        return False