#Contestador de celular
numero = int(input("ingrese un numero: "))
hora = int(input("ingrese una hora: "))
numero = str(numero)
if hora>=0 and hora <=7:
  print("CONTESTAR")
elif hora<14 and numero[-3:] == "909":
  print("CONTESTAR")
elif hora>=17 and hora<=19 and numero[0:3] == 887:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")