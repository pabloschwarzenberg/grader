#Contestador de celular
numero = int(input("Ingrese su numero de telefono de 8 cifras:"))
hora = eval(input("Ingrese una hora del 0 al 23: "))
#12345678
if hora<= 7:
  print("Contestar")
elif numero % 1000 == 909:
  print("Contestar")
elif hora<14:
  print("No contestar")
elif hora>=17 and hora<=19 and numero // 100000 != 877:
  print("Contestar")
elif hora>19:
  print("No contestar")
else:
  print("No contestar")
      