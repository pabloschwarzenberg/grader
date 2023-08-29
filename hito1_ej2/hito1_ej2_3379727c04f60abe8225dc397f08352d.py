#Contestador de celular
telefono = int(input("Ingrese telefono de 8 digitos: "))
while not(telefono>=10000000 and telefono<=99999999):
    telefono = int(input("ERROR..Telefono de 8 digitos: "))

hora = int(input("Ingrese la hora [0-23]: "))
while not(hora>=0 and hora<=23):
    hora = int(input("Error....Ingrese la hora [0-23]: "))

ultimostres = telefono%1000
primerostres = telefono//100000 #telefono=12345678

print(ultimostres)
print(primerostres)
#restriccion 1
if (hora>=0 and hora<=7):
  print("puedes CONTESTAR")
  
#restriccion 2  
elif (hora<14 and ultimostres != 909): #antes de las 14 después de las 7
  print("NO CONTESTAR")
elif (hora<14 and ultimostres == 909): #antes de las 14 después de las 7
  print("puedes CONTESTAR")

#restricción 3
elif (hora>=14 and hora<17):
  print("NO CONTESTAR")
elif (hora>=17 and hora<=19 and primerostres != 877):
  print("puedes CONTESTAR")
elif (hora>=17 and hora<=19 and primerostres == 877):
  print("NO CONTESTAR")
  
#restricción 4
else: #cualquier otro caso, o sea después de las 19
  print("NO CONTESTAR")