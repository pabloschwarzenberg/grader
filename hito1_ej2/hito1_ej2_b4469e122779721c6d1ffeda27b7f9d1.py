#numero de telefono 
print("ingrese el numero telefononico de 8 caracteres y la hora:")
numero=int(input("numero de celurar:>"))
print("ingrese la hora entre las 0 y 23:")
hora=int(input("ingrese la hora de la llamada:"))

x=numero%1000
 
if(numero<10000000) or (numero>99999999):
  print("el numero no existe, porfavor revisa que tenga 8 cifras")
elif(hora>=0 and hora<=7):
  print("contestar")
elif(hora>19 and hora<24):
  print(" no contestar")
elif(hora>23):
  print("hora no es valida entre 0 y 23")
elif(hora>=17 and hora<=19)and(numero>=87700000 and numero<=877999999):
  print("no contestar")
elif(hora>7 and hora<14)and(x==909):
  print("contestar")
elif(hora>7 and hora<14):
  print("no contestar")
else:
  print("contestar")