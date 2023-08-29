#Contestador de celular
numero = eval(input("ingrese un numero de telefono de 8 cifras "))
hora = eval(input("ingrese una hora "))
if (hora >= 0 and hora <= 7):
  print("CONTESTAR")
if (hora <= 14 and hora >= 8):
  if (numero > 910 or numero < 908):
    print("CONTESTAR")
  else:
     print("NO CONTESTAR")
if (hora >= 15 and hora <= 16):
  print("NO CONTESTA")
if (hora >= 17 and hora <= 19):
  if (numero > 87699999 and numero < 87800000):
    print("NO CONTESTAR")
  else:
     print("CONTESTAR")
if (hora >= 20):
  print("NO CONTESTAR")