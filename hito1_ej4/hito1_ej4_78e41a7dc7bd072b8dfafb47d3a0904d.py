#Conversión de Decimal a Binario
decimal = int(input("Ingresa un número decimal: "))
binario = ""

while decimal > 0:
    # Necesito saber si resto es 1 o 0 (para agregarlo al numero binario)
    residuo = int(decimal % 2)
    decimal = int(decimal / 2)
    # Una vez dividido, necesito agregar el residuo a la izquierda del binario
    binario = str(residuo) + binario
print("resultado=", binario)