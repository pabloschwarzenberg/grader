#Conversión de Decimal a Binario
valor = int(input("Ingrese un numero: "))
numero = valor
binario = ""
while numero>0:
  resto = int(numero%2)
  numero = int(numero//2)
  binario = str(resto) + binario
  bin = int(binario)

print(binario)