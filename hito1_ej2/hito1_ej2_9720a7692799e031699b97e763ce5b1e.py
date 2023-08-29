#Contestador de celular
numero = eval(input("ingrese numero de telefono:"))
hora = eval(input("ingrese hora (entre 0-23):"))
if(hora >= 0 and hora <= 7):
  print("contestar")
elif(hora < 14 and numero % 1000 == 909):
  print("contestar")
elif(hora >= 17 and hora <= 19 and not (numero // 100000 == 877)):
  print("contestar")
else:
  print("no contestar")