#Zodiaco
d = int(input("dia:"))
m = int(input("mes:"))
if d >= 21 and m == 3 or d <= 20 and m == 4:
  print("es de signo aries")
elif d > 20 and m == 4 or d <= 21 and m == 5:
  print("es de signo tauro")
elif d > 21 and m == 4 or d <= 21  and m == 6:
  print("es de signo geminis")
elif d > 21 and m == 6 or d >= 23 and m == 7:
  print("es de signo cancer")
elif d > 23 and m == 6 or d <= 23 and m == 8:
  print("es de signo leo")
elif d > 23 and m == 8 or d <= 23  and m == 9:
  print("es de signo virgo")
elif d > 23 and m == 9 or d <= 23 and m == 10:
  print("es de signo libra")
elif d > 23 and m == 10 or d <= 23 and m == 11:
  print("es de signo escorpio")
elif d > 22 and m == 11 or d <= 22 and m == 12:
  print("es de signo sagitario")
elif d > 22 and m == 12 or d <= 20 and m == 1:
  print("es de signo capricornio")
elif d > 20 and m == 1 or d <= 19 and m == 2:
  print("es de signo acuario")
elif d > 19 and m == 2 or d <= 21 and m == 3:
  print("es de signo piscis")