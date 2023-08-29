#Conversión de Decimal a Binario
num=eval(input("Ingrese su número\n"))
binario=(bin(num))
b=int(bin(num)[2:])
print("resultado=",b)