#Zodiaco
dia = int(input("Escriba el dia de si cumpleaños: "))
mes = int(input("Escriba el numero de mes de su cumpleaños: "))
if ((21 <= dia) and (mes == 3)) or ((dia < 20) and (mes == 4)):
  print("Aries")
elif ((20 <= dia) and (mes == 4)) or ((dia < 21) and (mes == 5)):
  print("Tauro")
elif ((21 <= dia) and (mes == 5)) or ((dia < 21) and (mes == 6)):
  print("Geminis")
elif ((21 <= dia) and (mes == 6)) or ((dia < 23) and (mes == 7)):
  print("Cancer")
elif ((23 <= dia) and (mes == 7)) or ((dia < 23) and (mes == 8)):
  print("Leo")
elif ((23 <= dia) and (mes == 8)) or ((dia < 23) and (mes == 9)):
  print("Virgo")
elif ((23 <= dia) and (mes == 9)) or ((dia < 23) and (mes == 10)):
  print("Libra")
elif ((23 <= dia) and (mes == 10)) or ((dia < 22) and (mes == 11)):
  print("Escorpio")
elif ((23 <= dia) and (mes == 11)) or ((dia < 22) and (mes == 12)):
  print("Sagitario")
elif ((22 <= dia) and (mes == 12)) or ((dia < 20) and (mes == 1)):
  print("Capricornio")
elif ((20 <= dia) and (mes == 1)) or ((dia < 19) and (mes == 2)):
  print("Acuario")
elif ((19 <= dia) and (mes == 2)) or ((dia < 21) and (mes == 3)):
  print("Piscis")