#Conversion de Decimal a Binario

n=int(input('ingrese un entero: '))
b=''
while n>0:
    d=n%2
    n=n//2
    b=str(d)+b

print("resultado= ",b)
 
 