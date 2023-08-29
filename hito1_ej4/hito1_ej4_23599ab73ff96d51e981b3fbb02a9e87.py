#Conversión de Decimal a Binario
print("CONVERSOR DECIMAL A BINARIO")
decimal=int(input("Ingrese el numero entero n a convertir: "))

binario=" "

while decimal>0:
    residuo=decimal%2
    decimal=decimal//2
    binario=str(residuo)+binario

print("Resultado =",binario)
      