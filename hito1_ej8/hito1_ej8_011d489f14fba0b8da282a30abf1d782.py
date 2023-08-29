#Descomponer un número
descomponer= int(input("Número natural de 1,2,3 o 4 cifras: "))

if 0<descomponer<10000:

  mil = descomponer//1000

  centena = (descomponer%1000)//100

  decena = ((descomponer%1000)%100)//10

  unidad = ((descomponer%1000)%100)%10

  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

else:

  print("El numero ingresado debe ser de 4 cifras")      