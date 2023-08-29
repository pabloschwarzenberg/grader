#Conversión de Decimal a Binario
# Entrada
x = int(input("Ingrese numero: "))
# Proceso
binario = bin(x)
y = (int(binario[2:]))
# Salida
print("resultado =",y)