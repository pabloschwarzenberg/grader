#Conversión de Decimal a Binario
n = int(input("Ingrese numero para transformarlo en decimal: "))
binario=""
if n > 0:
  while n > 0:
    binario = str(n%2) + binario
    n = n//2
  print("resultado=",binario)
elif n == 0:
  print("resultado=0")
      