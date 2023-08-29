#Contestador de celular
Numero = input()
Hora = int(input())
if Hora <= 7:
  print("CONTESTAR")
elif Hora > 7 and Hora <= 14 and Numero[-3:] == "909":
  print("CONTESTAR")
elif Hora >= 17 and Hora <= 19 and Numero[:3] != "877":
  print("CONTESTAR")
else:
  print("NO CONTESTAR")