#Zodiaco
DIA = int(input("Ingrese su dia de nacimiento: "))
MES = int(input("Ingrese su mes de nacimiento: "))

if (DIA >= 21 and MES == 3) or (DIA <= 20 and MES == 4):
  print("ARIES")
if (DIA >= 21 and MES == 4) or (DIA <= 20 and MES == 5):
  print("TAURO")
if (DIA >= 21 and MES == 5) or (DIA <= 21 and MES == 6):
  print("GEMINIS")
if (DIA >= 22 and MES == 6) or (DIA <= 22 and MES == 7):
  print("CÁNCER")
if (DIA >= 23 and MES == 7) or (DIA <= 22 and MES == 8):
  print("LEO")
if (DIA >= 23 and MES == 8) or (DIA <= 22 and MES == 9):
  print("VIRGO")
if (DIA >= 23 and MES == 9) or (DIA <= 22 and MES == 10):
  print("LIBRA")
if (DIA >= 23 and MES == 10) or (DIA <= 22 and MES == 11):
  print("ESCORPIO")
if (DIA >= 23 and MES == 11) or (DIA <= 21 and MES == 12):
  print("SAGITARIO")
if (DIA >= 22 and MES == 12) or (DIA <= 20 and MES == 1):
  print("CAPRICORNIO")
if (DIA >= 21 and MES == 1) or (DIA <= 18 and MES == 2):
  print("ACUARIO")
if (DIA >= 19 and MES == 2) or (DIA <= 20 and MES == 3):
  print("PISCIS")