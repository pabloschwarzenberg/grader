#Conversión de Decimal a Binario

numero=int(input("Ingrese un numero:"))
a= bin(numero)
b=int(a[2:])
print("resultado=",b)