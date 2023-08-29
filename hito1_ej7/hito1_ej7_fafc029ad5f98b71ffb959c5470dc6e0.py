#Zodiaco
D = int(input("Día:"))
M = int(input("Mes:"))

if D >= 21 and M == 3 or D <= 20 and M == 4:
  print("Su signo es Aries")
elif D > 20 and M == 4 or D <= 21 and M == 5:
  print("Su signo es Tauro")
elif D > 21 and M == 4 or D <= 21 and M == 6:
  print("Su signo es Geminis")
elif D > 21 and M == 6 or D <= 23 and M == 7:
  print("Su signo es Cancer")
elif D > 23 and M == 6 or D <= 23 and M == 8:
  print("Su signo es Leo")
elif D > 23 and M == 8 or D <= 23 and M == 9:
  print("Su signo es Virgo")
elif D > 23 and M == 9 or D <= 23 and M == 10:
  print("Su signo es Libra")
elif D > 23 and M == 10 or D <= 23 and M == 11:
  print("Su signo es Escorpio")
elif D > 22 and M == 11 or D <= 22 and M == 12:
  print("Su signo es Sagitario")
elif  D > 22 and M == 12 or D <= 20 and M == 1:
  print("Su signo es Capricornio")
elif D > 20 and M == 1 or D <= 19 and M == 2:
  print("Su signo es Acuario")
