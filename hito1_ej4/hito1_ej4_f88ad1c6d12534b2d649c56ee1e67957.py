#Conversión de Decimal a Binario
## ENTRADA DE DATOS - PROCESO - SALIDA DE DATOS     

Número_decimal = int(input("Ingrese un Número decimal: "))

binario = bin(Número_decimal)[2:]

print("resultado =", binario)