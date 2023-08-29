#Descomponer un número
n = int(input("ingrese un numero"))

if n <= 9999 and n >=0:

  milesima = n // 1000
  centena = (n - (milesima*1000))//100
  decena = (n - milesima*1000 -(centena*100))//10
  unidad = (n - milesima*1000 -centena*100 -(decena*10))//1
  print("%dM + %dC + %dD + %dU" % (milesima, centena, decena, unidad))