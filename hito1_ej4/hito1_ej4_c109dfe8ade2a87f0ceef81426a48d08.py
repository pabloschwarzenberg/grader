#Conversión de Decimal a Binario
decimal = float(input("ingrese su numero: "))
binario=""
if decimal <=0:
    print("su numero binario es 0")
while decimal>0:
    residuo = int(decimal%2)
    decimal=int(decimal/2)
    binario = str(residuo) + binario
resultado = binario
print("su resultado es =",resultado)