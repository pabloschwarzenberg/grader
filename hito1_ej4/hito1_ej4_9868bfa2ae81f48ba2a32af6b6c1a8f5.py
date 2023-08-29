#Conversión de Decimal a Binario
n=int(input("Ingrese un numero: "))

nb=""
while(n>0):
    print(n)
    if(n%2==0):
        nb=str(0)+nb
    else:
        nb=str(1)+nb
        
    n=n//2
print("resultado=", nb)      