#Contestador de celular
numero_de_telefono = eval(input("ingrese el numero telefonico de 8 digitos: "))
hora_de_llamada = eval(input("ingrese la hora de la llamada: "))

if (hora_de_llamada >= 0) and (hora_de_llamada <= 7):
  print("contestar")
elif (hora_de_llamada < 14) and (numero_de_telefono%1000 == 909):
  print("contestar")
elif (hora_de_llamada >= 17 and hora_de_llamada <= 19) and (numero_de_telefono%100000 == 877):
  print("contestar")
elif (hora_de_llamada >= 19 and hora_de_llamada < 0):
  print("contestar")
else:
  print("no contestar")