# por favor escribe aquí tu función
def es_primo(numero):
    #números para probar
    numeros=[2,3,4,5,6,7,8,9]
    #si numero es 1 no es primo
    if  numero==1:
        return False
    #si el número es igual a algún número de la lista
    #quitar número de la lista
    for i in numeros:
        if i==numero:
            numeros.remove(i)
    #si el número dividido por un numero distinto a él, entrega como resto 0
    #no es primo
    for i in numeros:
        if numero%i==0:
            return False
    #si dividido por el mismo y por 1, entrega como resto 0, es primo
    if numero%numero==0 and numero%1==0:
        return True