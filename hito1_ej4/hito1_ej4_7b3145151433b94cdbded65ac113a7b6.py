numero = int(input("Ingrese un numero decimal para convertir a binario:"))

resto=''

while numero//2 != 0:
  resto = str(numero%2) + resto
  numero = numero//2

  binario = str(numero) + resto

print("resultado =",binario)