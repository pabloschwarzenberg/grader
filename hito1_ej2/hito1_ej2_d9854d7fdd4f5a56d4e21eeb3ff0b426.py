#Contestador de celular
num_telefono = int(input("ingrese numero telefonico: "))
hora = int(input("ingese hora de llamada: "))

if hora >= 0 and hora <= 7:
  print("contestar")
elif hora < 14:
  if num_telefono % 1000 == 909:
    print("contestar")
  else :
    print("no contestar")
elif hora >= 17 and hora <= 19:
  if num_telefono % 1000000 == 877:
    print ("no contestar")
  else :
    print("contestar")
elif hora > 19:
  print("no contestar")