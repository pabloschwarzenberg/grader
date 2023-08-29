#Contestador de celular
telefono = input("ingrese numero telefonico: ")
hora = int(input("ingrese hora de la llamada: "))
if 0<=hora<=7:
  print("CONTESTAR")
if hora < 14 and telefono[5::] != "909":
  print("NO CONTESTAR")
if hora < 14 and telefono[5::] == "909":
  print("CONTESTAR")
if 17 < hora < 19 and telefono[:3:] == "877":
  print("NO CONTESTAR")
if 17 < hora < 19 and telefono[:3:] != "877":
 print("CONTESTAR")
if hora > 19 :
  print("NO CONTESTAR")