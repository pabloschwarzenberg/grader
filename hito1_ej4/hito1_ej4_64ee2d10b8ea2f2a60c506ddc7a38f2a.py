#Conversión de Decimal a Binario
decimal = int(input())
  
resultado = ''
while decimal > 0:
  residuo = decimal % 2
  resultado += str(residuo)
  decimal = decimal // 2

print("resultado = {}".format(resultado[::-1]))