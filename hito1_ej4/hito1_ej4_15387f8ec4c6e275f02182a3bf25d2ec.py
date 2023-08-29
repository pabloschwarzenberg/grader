#Conversión de Decimal a Binario
#numero_d = decimal
print("DE DECIMAL A BINARIO")
numero_d = int(input("Ingrese un numero: "))
binario = " "
print("El numero que escogiste es: ", numero_d)
while numero_d>0:
  resto = numero_d % 2
  numero_d = numero_d // 2
  binario = str(resto)+binario
print("resultado=", binario)      