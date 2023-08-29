A = int(input("Ingresa un numero de máximo 4 cifras: "))

if 0<A<10000:

  miles = A//1000

  centena = (A%1000)//100

  decena = ((A%1000)%100)//10

  unidad = ((A%1000)%100)%10

  print(str(miles)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

else:

  print("Numero incorrecto")


  