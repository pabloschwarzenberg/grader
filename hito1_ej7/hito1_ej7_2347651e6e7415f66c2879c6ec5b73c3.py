#Zodiaco
D = int(input("ingrese su dia de nacimiento: "))
M = int(input("ingrese su mes de nacimiento: "))

if 21 < D <= 31 and M == 3:
   print("Aries")
elif D <= 20 and M == 4:
   print("Aries")
elif 20 < D <= 30 and M == 4:
   print("Tauro")
elif D <= 21 and M == 5:
   print("Tauro")
elif 21 < D <= 31 and M == 5:
   print("Geminis")
elif D <= 21 and M == 6:
   print("Geminis")
elif 21 < D <= 30 and M == 6:
   print("Cancer")
elif D <= 23 and M == 7:
   print("Cancer")
elif 23 < D <= 31 and M == 7:
   print("Leon")
elif D <= 23 and M == 8:
   print("Leon")
elif 23 < D <= 31 and M == 8:
   print("Virgo")
elif D <= 23 and M == 9:
   print("Virgo")
elif 23 < D <= 30 and M == 9:
   print("Libra")
elif D <= 23 and M == 10:
   print("Libra")
elif 23 < D <= 31 and M == 10:
   print("Escopion")
elif D <= 22 and M == 11:
   print("Escorpion")
elif 22 < D <= 30 and M == 11:
   print("Sagitario")
elif D <= 22 and M == 12:
   print("Sagitario")
elif 22 < D <= 31 and M == 12:
   print("Capricornio")
elif D <= 20 and M == 1:
   print("Capricornio")
elif 20 < D <= 31 and M == 1:
   print("Acuario")
elif D <= 19 and M == 2:
   print("Acuario")
elif 19 < D <= 29 and M == 2:
   print("Piscis")
elif D <= 21 and M == 3:
   print("Piscis")
else:
   print("Los numeros no corresponden a dia ni a mes")      