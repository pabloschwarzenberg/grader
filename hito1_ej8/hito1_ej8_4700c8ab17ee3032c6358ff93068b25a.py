#Descomponer un número
num = int(input("Número de hasta 4 dígitos: "))

if 0<num<10000:
  mil = num//1000
  cen = (num%1000)//100
  dec = ((num%1000)%100)//10
  un = ((num%1000)%100)%10
  print(mil,"M +",cen,"C +",dec,"D +",un,"U")      