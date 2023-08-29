#Conversión de Decimal a Binario
decimal=int(input("Ingrese un número cualquiera: "))
a=bin(decimal)
a=a[2:]
print("Resultado= ", a)