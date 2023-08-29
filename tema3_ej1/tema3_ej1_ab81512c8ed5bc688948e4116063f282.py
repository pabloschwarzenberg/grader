# completa el código de la función
def suma_divisores(n):
    enteros=list(range(0,n+1))
    entero=enteros[1:n]
    divisores=[]
    for divisor in entero:
        resto=n%int(divisor)
        if resto==0:
            divisores.append(divisor)
    if n==1:
        return 0,False
    suma=0
    for sumando in divisores:
        suma+=int(sumando)
    if suma==1:
        return suma,True
    elif suma>1:
        return suma,False
           