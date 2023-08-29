#Factores Primos
#PORQUEEEEE
numero=int(input())
#tiene que ser mayor de 2 sino divide por 0 y 1, y explota o dice que todos los numeros lo son cuando divide por 1
factor=2

while(numero>1):
    # no se si tira loop infinito, no debería
    if(numero%factor==0):
        print(factor)
        numero=numero // factor
    else:
        factor=factor+1
        # esto funciona o no?