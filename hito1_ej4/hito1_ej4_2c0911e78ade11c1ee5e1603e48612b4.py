#Conversión de Decimal a Binario
     
a = int(input())

s = str()
while a > 0:
      s = s + str(a%2)
      a = a // 2
      print("resultado= ", s[::-1])