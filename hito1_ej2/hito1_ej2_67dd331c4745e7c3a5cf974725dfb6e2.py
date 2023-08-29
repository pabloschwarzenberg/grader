#Contestador de celular
telefono = int(input("Ingrese su numero de telefono: "))
hora = int(input("Ingrese la hora: "))
l = list(str(telefono))
h = list(str(hora))
e = ["1","2","3","4","5","9","0","9"]
e2 = ["8","7","7"]

if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora>7 and hora<=14 and l[5:8] == e[5:8]:
  print("CONTESTAR")
elif hora>7 and hora<=14 and l[5:8] != e[5:8]:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and l[0:3] == e2[0:3]:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and l[0:3] != e2[0:3]:
  print("CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")      