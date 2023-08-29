# completa el código de la función
def suma_divisores(numero):
    divisor=[1]
    for i in range(2,numero): 
        if numero%i==0:
            divisor.append(i)
    suma=sum(divisor) 
    if suma==1: ### si la suma es 1 es primo
        if numero ==1:## Caso Borde
            return(0,False)
        else:
            return(suma,True)
    else:  ### caso contrario no es primo
        return(suma,False)
