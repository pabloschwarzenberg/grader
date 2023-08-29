#Conversión de Decimal a Binario
a = float(input("Ingrese un número: "))
a = int(a)
a = bin(a).replace("0b" , "")
print("resultado=",a)