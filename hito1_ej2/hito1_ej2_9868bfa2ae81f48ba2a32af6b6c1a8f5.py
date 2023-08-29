#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
if hora >= 0 and hora<=7:
  print("CONTESTAR")
elif numero%1000==909:
  print("CONTESTAR")
elif hora<14:
  print("NO CONTESTAR")
elif numero//100000==877:
  print("NO CONTESTAR")
elif hora>= 17 and hora<=19:
  print("CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")