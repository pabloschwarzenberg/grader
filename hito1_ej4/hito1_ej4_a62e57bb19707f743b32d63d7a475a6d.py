#Conversión de Decimal a Binario
x=int(input("Introducir un numero decimal: "))
bin=""
while x!=0:
    x_1=x%2
    x=x//2
    bin=str(x_1)+bin
print("resultado=",bin)