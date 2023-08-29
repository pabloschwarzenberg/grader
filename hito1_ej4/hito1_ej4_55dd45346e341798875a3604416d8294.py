#Conversión de Decimal a Binario
num = int(input("Ingrese un número decimal:"))
binario = ""
residuo = 0
while num != 0:
  residuo = num%2
  aux = str(residuo)
  binario = binario + aux
  num //=2
print("resultado="+binario[::-1])