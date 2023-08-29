#Zodiaco
d = int(input("Ingrese su día de nacimiento uwu: "))

while d < 0 or d >= 31:

  print("Dato inválido >:c.")
  d = int(input("Ingrese su día de nacimiento: "))

m = int(input("ingrese su mes de nacimiento owo: "))

while m < 0 or m > 12:

  print("Dato inválido >:c.")
  m = int(input("Ingrese su mes de nacimiento: "))

#aries: 21 de marzo - 20 de abril
if (d >= 21 and m == 3) or (d <= 20 and m == 4):

  print("Aries")

#tauro: 21 de abril - 20 de mayo

elif (d >= 21 and m == 4) or (d <= 20 and m == 5):

  print("Tauro")

#geminis: 21 de mayo - 21 de junio
elif (d >= 21 and m == 5) or (d <= 21 and m == 6):

  print("Geminis") 


elif (d >= 22 and m == 6) or (d <= 22 and m == 7):

  print("Cancer")

elif (d >= 23 and m == 7) or (d <= 22 and m == 8):

  print("Leo")


elif (d >= 23 and m == 8) or (d <= 22 and m == 9):

  print("Virgo")

elif (d >= 23 and m == 9) or (d <= 22 and m == 10):

  print("Libra")

elif (d >= 23 and m == 10) or (d <= 22 and m == 11):

  print("Escorpio") 

elif (d >= 23 and m == 11) or (d <= 21 and m == 12):

  print("sagitario")

elif (d >= 22 and m == 12) or (d <= 20 and m == 1):

  print("Capricornio")

elif (d >= 21 and m == 1) or (d <= 18 and m == 2):

  print("Acuario") 

elif (d >= 19 and m == 2) or (d <= 20 and m == 3):

  print("Picis")      