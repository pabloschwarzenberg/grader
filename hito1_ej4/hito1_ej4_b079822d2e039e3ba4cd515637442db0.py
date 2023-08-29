#Conversión de Decimal a Binario
decimal = eval(input("ingrese numero decimal: "))
binario =" "
while decimal > 0:
  residuo=decimal%2
  decimal=decimal//2
  binario=str(residuo) + binario
print("resultado=",binario)    