# por favor escribe aquí tu función
def es_primo(n):
    enteros=list(range(0,n+1))
    entero=enteros[1:n]
    divisores=[]
    for divisor in entero:
        resto=n%int(divisor)
        if resto==0:
            divisores.append(divisor)
    if n==1:
        return False
    suma=0
    for sumando in divisores:
        suma+=int(sumando)
    if suma==1:
        return True
    elif suma>1:
        return False
           