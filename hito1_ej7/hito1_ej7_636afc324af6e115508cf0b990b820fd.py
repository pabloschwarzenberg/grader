#Zodiaco
D= int(input("Dia: "))
M= int(input("Mes: "))

if D >=21 and M == 3 or D <= 20 and M == 4:
  print("Su signo es aries")
elif D > 20 and M == 4 or D <= 21 and M ==5:
  print("su signo es tauro")
elif D > 21 and M == 4 or D <= 21 and M == 6:
  print("su signo es geminis")
elif D > 21 and M == 6 or D >= 23 and M == 7:
  print("Su signo es cancer")
elif D > 23 and M == 6 or D <= 23 and M == 8:
  print("su signo es leo")
elif D > 23 and M == 8 or D <= 23 and M == 9:
  print("su signo es virgo")
elif D > 23 and M == 9 or D <= 23 and M == 10:
  print("su signo es libra")
elif D > 23 and M == 10 or D <= 23 and M == 11:
  print("su signo es escorpio")
elif D > 22 and M == 11 or D <= 22 and M == 12:
  print("su signo es sagitario")
elif D > 22 and M == 12 or D <= 20 and M == 1:
  print("su signo es capricornio")
elif D > 20 and M == 1 or D <= 19 and M == 2:
  print("su signo es acuario")
elif D > 19 and M == 2 or D <= 21 and M == 3:
  print("su signo es piscis")