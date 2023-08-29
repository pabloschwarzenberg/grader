#Descomponer un número
x = int(input("Adjunte cualquier número natural hasta 4 cifras: "))

if 0<x<10000:

  mil = x //1000

  centena = (x%1000)//100

  decena = ((x%1000)%100)//10

  unidad = ((x%1000)%100)%10

  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

