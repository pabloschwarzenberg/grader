#Conversión de Decimal a Binario
decimal = int(input())
binario = " "

while decimal > 0:
  s=decimal%2
  decimal=decimal//2
  binario=str(s)+binario
print('resultado=', binario)