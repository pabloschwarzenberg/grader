#Conversión de Decimal a Binario
decimal = float(input("Ingrese un número decimal: "))
binario = ""
while decimal != 0:
    cociente = decimal//2
    resto = decimal%2
    decimal = cociente
    resto = int(resto)
    resto = str(resto)
    binario = resto + binario
binario = int(binario)
print("resultado=",binario)