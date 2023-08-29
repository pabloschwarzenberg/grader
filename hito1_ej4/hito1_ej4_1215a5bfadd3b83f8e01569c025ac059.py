#Conversión de Decimal a Binario
binario=int(input("ingrese un numero decimal: "))
bin(binario)
a=int(bin(binario)[2:])
print("resultado=",a)