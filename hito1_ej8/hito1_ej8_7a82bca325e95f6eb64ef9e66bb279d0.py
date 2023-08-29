#Descomponer un número
n = int(input())
if 10000 > n > 999:
  unidades = (n % 10)
  decenas = (n % 100) // 10
  centenas = (n % 1000) // 100
  miles = (n % 10000) // 1000
  print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U", sep = "")
elif 1000 > n > 99:
  unidades = (n % 10)
  decenas = (n % 100) // 10
  centenas = (n % 1000) // 100
  miles = (n % 10000) // 1000
  print(centenas,"C","+",decenas,"D","+",unidades,"U", sep = "")
elif 100 > n > 9:
  unidades = (n % 10)
  decenas = (n % 100) // 10
  centenas = (n % 1000) // 100
  miles = (n % 10000) // 1000
  print(decenas,"D","+",unidades,"U", sep = "")
elif 10 > n > 0:
  unidades = (n % 10)
  decenas = (n % 100) // 10
  centenas = (n % 1000) // 100
  miles = (n % 10000) // 1000
  print(unidades,"U", sep = "")            