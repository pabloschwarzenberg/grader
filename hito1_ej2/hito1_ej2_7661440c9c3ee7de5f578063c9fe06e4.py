#Contestador de celular
numero = (input("introduzca su numero de telefono"))
hora = int(input("ingrese la hora de llamada"))
pd = int(numero[0]+numero[1]+numero[2])
ud = int(numero[5]+numero[6]+numero[7])

if hora>=0 and hora<=7:
  print("contestar")
if hora>7 and hora<14 and ud==909:
  print("contestar")
if hora>=17 and hora<=19 and pd==877:
  print(" no contestar")  
elif hora>=17 and hora<=19:
    print("contestar")
if hora>19 and hora<23:
  print("no contestar")

