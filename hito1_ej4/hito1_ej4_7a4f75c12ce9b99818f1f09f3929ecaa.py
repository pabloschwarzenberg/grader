#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número para convertirlo a binario: "))
binario = ""
while decimal - 1 != 0:
  if decimal % 2 == 0:
    binario += "0"
    decimal = decimal / 2
  elif decimal % 2 == 1:
    binario += "1"
    decimal = int(decimal/2)
binario += "1"
binariof = ""
for letra in binario:
  binariof = letra + binariof
print("resultado =", binariof)