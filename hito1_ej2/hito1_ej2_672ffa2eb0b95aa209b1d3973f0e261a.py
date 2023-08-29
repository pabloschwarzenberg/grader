#Contestador de celular
numero = str(input("ingrese su numero celular: "))
hora = int(input("ingrese la hora: "))

for i in range(len(numero)5, 7)):
  if i == numero[5:7]

if int(numero) < 100000000 and hora >= 0 and hora <= 7:
  print("contestar")
elif int(numero) < 100000000 and hora < 14 and hora > 7:
  print("no contestar")
elif numero[5:7] == 909 and hora < 14 and hora > 7:
  print("contestar")
elif int(numero) < 100000000 and hora >= 17 and hora <= 19:
  print("contestar")
elif numero[0:2] == 877 and hora >= 17 and hora <= 19:
  print("no contestar")
elif hora > 19:
  print("no contestar")
else:
  print("no contestar")      