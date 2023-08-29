#Contestador de celular
numero = int(input("ingrese el numero telefonico"))
horas = int(input("ingrese una hora que sea entre las 0 hrs y las 23 hrs"))

if horas>=0 and horas<=7:
  print("CONTESTAR")
elif numero % 1000 == 909:
  print("CONTESTAR")
elif horas>=17 and horas<19 and numero // 100000 != 877:
  print("CONTESTAR")
elif horas >=19 :
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")