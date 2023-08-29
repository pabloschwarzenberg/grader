#Conversión de Decimal a Binario
decimal = int(input("ingrese un numero decimal:"))

binario = " "
print("Tu numero",decimal)
while decimal > 0:
    residuo = decimal % 2
    decimal = decimal // 2
    binario = str(residuo)+binario

print("resultado= ", binario)    

