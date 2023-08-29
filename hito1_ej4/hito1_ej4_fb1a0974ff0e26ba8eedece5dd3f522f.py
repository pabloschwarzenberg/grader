#Conversión de Decimal a Binario
n=int(input("Numero:"))
b=" "
while n>1:
    if n%2==0:
        b="0"+b
        n=int(n/2)
        print(n)
    else:
        b="1"+b
        n=int(n/2)
        print(n)
if n==1:
    b="1"+b
else:
    b="0"+b
print("Resultado=",b)