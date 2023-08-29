#Contestador de celular
numero = eval(input("ingrese numero telefonico"))
hora = eval(input("Ingrese hora de llamada"))
if(hora >= 0 and hora <= 7):
  print("Contestar llamada")
elif(hora < 14 and numero % 1000 == 909):
  print("Contestar llamada")
elif(hora >= 17 and hora <= 19 and not (numero // 100000 == 877)):
  print("Contestar llamada")
else:
  print("No contestar llamada")    