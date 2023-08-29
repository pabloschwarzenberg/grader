#Conversión de Decimal a Binario
def transfbin(decimal):
  bin = ""
  while decimal // 2 != 0:
    bin = str(decimal % 2) + bin
    decimal = decimal // 2
  return str(decimal) + bin
numero = int(input("Introduzca el número decimal para convertir a binario: "))
print("resultado=",transfbin(numero))