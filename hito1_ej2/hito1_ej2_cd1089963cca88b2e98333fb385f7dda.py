#Contestador de celular
telefono=int(input("ingrese su numero de telefono de 8 digitos: "))
while not (telefono>=10000000 and telefono<=99999999):
  telefono=int(input("Error... vuelva a ingresar su numero de telefono de 8 digitos: "))
hora=int(input("ingrese la hora de la llamada [0-23]: "))
while not(hora>=0 and hora<=23):
  hora=int(input("hora incorrecta, vuelva a ingresar la hora [0-23] : "))
ultimostres=telefono%1000
primerostres=telefono//100000
if (hora<=7 and hora>=0):
  print("CONTESTAR")
  
elif (hora<14 and ultimostres!=909 ):
  print("NO CONTESTAR")
elif (hora<14 and ultimostres==909):
  print("CONTESTAR")

elif (hora>14 and hora<17):
  print("NO CONTESTAR")
elif (hora>17 and hora<19 and primerostres!=877):
  print("NO CONTESTAR")
elif (hora>17 and hora<19 and primerostres==877):
  print("CONTESTAR")

elif (hora>19):
  print("NO CONTESTAR")