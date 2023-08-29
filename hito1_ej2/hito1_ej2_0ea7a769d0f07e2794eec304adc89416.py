#Contestador de celular
numero=int(input("ingrese un numero de telefono de 8 digitos "))
while(numero<10000000 or numero>=100000000):
  print("numero invalido")
  numero=int(input("ingrese un numero de telefono de 8 digitos "))
print("numero valido")


ultimos_digitos= numero % 1000
primeros_digitos=int (numero /100000)

hora=int(input("ingrese la hora de llamado "))
while(hora<0 or hora>23):
  print("horario incorrecto")
  hora=int(input("ingrese la hora de llamado "))
if(hora>=0 and hora<=7):
   print("CONTESTAR")
elif(hora >=8 and hora<=14):
  if ultimos_digitos== 909:
    print("contestar")
elif(hora >=8 and hora<=14):
  print("no contestar")
elif(hora>14 and hora<=16):
  print("no contestar")
elif(hora>=17 and hora<=19):
  if primeros_digitos== 877:
    print("no contestar")
elif(hora>=17 and hora<=19):
  print("CONTESTAR")
elif(hora>19 and hora<=23):
  print("no contestar") 