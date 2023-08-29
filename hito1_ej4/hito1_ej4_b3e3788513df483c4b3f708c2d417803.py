#Conversión de Decimal a Binario
num = int(input("ingresar un número decimal: "))
binario = 0
posicion = 1

while num > 0:
  resto = num % 2
  binario += resto * posicion
  posicion *= 10
  num //= 2

print("resultado =", binario)