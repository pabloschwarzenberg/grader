#Zodiaco
print("Hola, soy tu horoscopo y vere cual es tu signo")
dia=int(input("Ingrese su dia de nacimiento:"))
mes=int(input("Ingrese su mes de nacimiento:"))
if (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
  print("A usted se le designa el signo Acuario")
if (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
  print ("A usted se le designa el signo Piscis")
if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
  print ("A usted se le asigna el signo Aries")
if (dia >= 21 and mes == 4) or (dia <= 21 and mes == 5):
  print("A usted se le asignara el signo Tauro")
if (dia >= 22 and mes == 5) or (dia <= 21 and mes == 6):
  print("A usted se le asigna el signo Geminis")
if (dia >= 21 and mes == 6) or (dia <= 23 and mes == 7):
  print ("A usted se le asigna el signo Cancer")
if (dia >= 24 and mes == 7) or (dia <= 23 and mes == 8):
  print("A usted se le asigna el signo Leo")
if (dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
  print("A usted se le asigna el signo Virgo")
if (dia >= 24 and mes == 9) or (dia <= 23 and mes == 10):
  print("A usted se asigna el signo Libra")
if (dia >= 24 and mes == 10) or (dia <= 22 and mes == 11):
  print ("A usted se le asigna el signo Escorpio")
if (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
  print ("A usted se le asigna el signo Sagitario")
if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
  print ("A usted se le asigna el signo Capricornio")