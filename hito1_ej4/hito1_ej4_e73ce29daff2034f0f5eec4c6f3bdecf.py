#Conversión de Decimal a Binario
n=int(input("ingrese un numero: "))
x=""
while True :
    if n==2:
        x="10"+x
        break
    if n==1:
        x="1"+x
        break
        
    if n%2==0 :
        x=str(0)+x
        n=n/2
        
    if n%2==1:
        x=str(1)+x
        n=(n-1)/2

print("Resultado=",end="")
print(x)      