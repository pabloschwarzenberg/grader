numero = int(input("Ingrese numero a convertir: "))
binario = ""
while numero > 0:
  binario = str(numero % 2) + binario
  numero = numero//2
print("resultado=", binario)