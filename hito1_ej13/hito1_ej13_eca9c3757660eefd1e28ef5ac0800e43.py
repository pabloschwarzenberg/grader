#Factores Primos
factor=2
numero=int(input("Ingrese el número a descomponer:"))

while(factor<=numero):
    
    if not numero%factor!=0:
        print(factor)
        numero/=factor
    else:
        factor+=1