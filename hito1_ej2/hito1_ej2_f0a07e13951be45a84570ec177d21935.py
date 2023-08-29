#Contestador de celular
numero_telefonico=int(input("ingrese numero de 8 digitos"))
hora=int(input("ingrese hora de llamada"))
if hora >0 and hora<7:
  print("CONTESTAR")
elif hora<14 and numero_telefonico%1000==909:
  print("CONTESTAR")
elif hora>=17 and hora<=19 or numero_telefonico//10000==877:
  print("CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")

     