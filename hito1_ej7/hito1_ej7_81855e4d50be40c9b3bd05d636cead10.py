D = eval(input("Día: "))
M = eval(input("Mes: "))

if 21 <= D <= 31 and M == 3 or 1 <= D <= 20 and M == 4:
  print("Aries")
elif 20 <= D <= 30 and M == 4 or 1 <= D <= 21 and M == 5:
  print("Tauro")
elif 21 <= D <= 31 and M == 5 or 1 <= D <= 21 and M == 6:
  print("Géminis")
elif 21 <= D <= 30 and M == 6 or 1 <= D <= 23 and M == 7:
  print("Cáncer")
elif 23 <= D <= 31 and M == 7 or 1 <= D <= 23 and M == 8:
  print("Leo")
elif 23 <= D <= 31 and M == 8 or 1 <= D <= 23 and M == 9:
  print("Virgo")
elif 23 <= D <= 30 and M == 9 or 1 <= D <= 23 and M == 10:
  print("Libra")
elif 23 <= D <= 31 and M == 10 or 1 <= D <= 22 and M == 11:
  print("Escorpio")
elif 22 <= D <= 30 and M == 11 or 1 <= D <= 22 and M == 12:
  print("Sagitario")
elif 22 <= D <= 31 and M == 12 or 1 <= D <= 20 and M == 1:
  print("Capricornio")
elif 20 <= D <= 31 and M == 1 or 1 <= D <= 19 and M == 2:
  print("Acuario")
elif 19 <= D <= 29 and M == 2 or 1 <= D <= 21 and M == 3:
  print("Piscis")