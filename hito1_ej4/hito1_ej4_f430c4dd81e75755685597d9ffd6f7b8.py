#Conversión de Decimal a Binario
a=int(input("ingrese número a convertir"))
b=bin(a)
c=b.lstrip("0b")
print("resultado=",c)