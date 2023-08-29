#Contestador de celular
numero = str(input("Ingrese numero telefonico:"))
hora = int(input("Ingrese hora de llamada: "))

if 0 <= hora <= 7:
  print("CONTESTAR")
elif 7 < hora <= 14 and numero[5:8] != "909":
  print("NO CONTESTAR")
elif 7 < hora <= 14 and numero[5:8] == "909":
    print("CONTESTAR")
elif 17 <= hora <=19 and numero[0:3] != "877":
  print("CONTESTAR")
elif 17 <= hora <=19 and numero[0:3] == "877":
  print("NO CONTESTAR")
elif 19 < hora <= 23:
  print("NO CONTESTAR")     