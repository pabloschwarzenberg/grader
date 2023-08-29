#Contestador de celular
telefono = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
telefono = str(telefono)
#print(type(telefono))
cadena1 = ""
cadena2 = ""
for n in range(5,8) :
  cadena1 = str(cadena1) + telefono[n]
 # print(cadena1)
#print(len(cadena1))

for n in range(0,3) :
  cadena2 = str(cadena2) + telefono[n]
 # print(cadena2)
#print(len(cadena2))
cadena1 = int(cadena1)
cadena2 = int(cadena2)
if hora > 0 and hora <= 7 :
  print("emergencia contestar")

elif hora > 7 and hora <= 14 :
  if cadena1 == 909 :
    print("contestar")
  else :
    print("no contestar")

elif hora > 14 and hora <= 19 :
  if cadena2 == 877 :
    print("no contestar")
  else :
    print("contestar")

elif hora > 19 :
  print("no contestar")     