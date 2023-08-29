#Contestador de celular
llamada=int(input("Ingrese numero telefonico de 8 digitos: "))
hora=int(input("Ingrese la hora de llamda de 00:00 a 23:00: "))

if 0<=hora<=7:
  print("Contestar")
elif hora<14 and llamada%100==9:
  print("Contestar")
elif 19>hora>=17 and(llamada//1000000==877):
  print("Contestar")
else:
  print("No contestar")