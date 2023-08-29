#Contestador de celular
hora = int(input("Ingrese la hora: "))
num = int(input("Ingrese el numero de 8 digitos: "))
if ((hora >= 0) and (hora <= 7)) or (hora >= 17) and (hora <= 19):
  if (num < 87800000) and (num > 87699999):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif (hora > 14) and (num% == 3):
    print("CONTESTAR")
else:
  print("NO CONTESTAR") 