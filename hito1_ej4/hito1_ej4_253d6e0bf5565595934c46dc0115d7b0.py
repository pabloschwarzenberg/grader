#Conversión de Decimal a Binario
x=int(input("ingrese un numero decimal"))
x1=bin(x)
y=str(x1)
b=int(y[2:])
print("resultado=",b)