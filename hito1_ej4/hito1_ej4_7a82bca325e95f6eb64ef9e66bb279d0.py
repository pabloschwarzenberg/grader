#Conversión de Decimal a Binario
n = eval(input())

while n > 0 :
  resto = n % 2
  print(resto)
  n = n // 2
      