#Conversión de Decimal a Binario
a=eval(input("Ingrese Numero Decimal= "))
binario=(bin(a))
r=int(bin(a)[2:])
print("Resultado= ",r)     