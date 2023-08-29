def numero_perfecto(a):
    enteros=list(range(0,a+1))
    entero=enteros[1:a]
    divisores=[]
    for divisor in entero:
        resto=a%int(divisor)
        if resto==0:
            divisores.append(divisor)
    if a==1:
        return False
    suma=0
    for sumando in divisores:
        suma+=int(sumando)
    if suma==a:
        return True
    else:
        return False