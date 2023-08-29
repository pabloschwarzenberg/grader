numero = int(input("ingrese el numero telefonico "))
hora = int(input("ingrese la hora de la llamada "))

if numero > 99999999: 
  print("ingrese un numero de telefono existente")
elif hora < 0 or hora > 23:
  print("ingrese una hora existente ")
else:
  print("numero y hora de llamada correctas ")

if hora >= 0 and hora <= 7:
  print("CONTESTAR")
elif hora > 7 and hora <= 14:
  numero = str(numero)
  if numero[5]+numero[6]+numero[7] == str(9)+str(0)+str(9):
    print("CONTESTAR")
  else: 
    print("NO CONTESTAR")
elif hora > 14 and hora <= 16:
  print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
  numero = str(numero)
  if numero[0]+numero[1]+numero[2] == str(8)+str(7)+str(7):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif hora > 19 and hora <= 23:
  print("NO CONTESTAR")