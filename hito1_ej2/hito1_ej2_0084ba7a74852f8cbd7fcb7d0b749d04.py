#Contestador de celular
num = int(input("Ingrese numero: "))
hora = int(input("Ingrese hora: "))    
n = str(num)
if  0 <= hora <= 7:
  print("CONTESTAR")
elif hora < 14 and n[5:] != "909":
  print("NO CONSTESTAR")
elif hora < 14 and n[5:] == "909":
  print("CONTESTAR")
elif 17 <= hora <= 19 and n[:3] == "877":
  print("NO CONTESTAR")
elif 17 <= hora <= 19 and n[:3] != "877":
  print("CONTESTAR")
elif hora > 19:
  print("NO CONTESTAR")