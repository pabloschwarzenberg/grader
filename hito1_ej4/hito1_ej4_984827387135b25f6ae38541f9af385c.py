#Conversión de Decimal a Binario
decimal = int(input("Ingrese un numero que quiera convertir a binario: "))
binario = ""
while decimal > 0:
    residuo = int(decimal % 2)
    decimal = int(decimal / 2)
    binario = str(residuo) + binario
print("resultado=", binario)