#Contestador de celular
telefono = int(input("ingrese numero de 8 digitos:"))
hora = eval(input("ingrese hora (0-23):"))

x = telefono//100000
y = telefono %1000

if hora <= 7 and hora >= 0:
  print("CONTESTAR")
elif hora > 19:
  print("NO CONTESTAR")
elif hora < 14 and y == 909:
  print("CONTESTAR")
elif hora >= 17 and hora <=19 and x != 877:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")