#Conversión de Decimal a Binario
a=int(input("ingrese numero: "))
b=str(bin(a))
c=b.lstrip("0b")
print("resultado= ",c)