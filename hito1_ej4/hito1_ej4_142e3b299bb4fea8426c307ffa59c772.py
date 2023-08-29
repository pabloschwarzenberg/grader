#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

negativo = False
if (decimal<0):
    negativo=True
    decimal=abs(decimal)

binario= bin(decimal)[2:]

if (negativo):
    binario = ("-" + binario)

print("resultado= ", binario) 