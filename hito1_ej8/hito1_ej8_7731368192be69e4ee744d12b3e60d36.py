#Descomponer un número
num = int(input())
if num > 0:
  mil = num//1000
  centena = (num%1000)//100
  decena = ((num%1000)%100)//10
  unidad = ((num%1000)%100)%10
  print(mil, "M +", centena, "C +", decena, "D +", unidad, "U")