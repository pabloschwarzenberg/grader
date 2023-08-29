#Zodiaco
dia=input("dia: ")
mes=input("mes: ")

if (len(dia) == 1):
  dia = "0" + dia

if (len(mes) == 1):
  mes = "0" + mes

fecha = mes + dia

if (fecha >= "0321" and fecha < "0420"):
  print("Aries")
elif (fecha >= "0420" and fecha < "0521"):
  print("Tauro")
elif (fecha >= "0521" and fecha < "0621"):
  print("Géminis")
elif (fecha >= "0621" and fecha < "0723"):
  print("Cáncer")
elif (fecha >= "0723" and fecha < "0823"):
  print("Leo")
elif (fecha >= "0823" and fecha < "0923"):
  print("Virgo")
elif (fecha >= "0923" and fecha < "1023"):
  print("Libra")
elif (fecha >= "1023" and fecha < "1123"):
  print("Escorpio")
elif (fecha >= "1123" and fecha < "1222"):
  print("Sagitario")
elif (fecha >= "1222" or fecha < "0120"):
  print("Capricornio")
elif (fecha >= "0120" and fecha < "0219"):
  print("Acuario")
else:
  print("Piscis")