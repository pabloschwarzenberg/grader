#Zodiaco
dia = int(input("dia de tu cumpleaños: "))
mes = int(input("mes de cumpleaños del 1 al 12: "))

if mes == 1 and dia <= 20 or mes == 12 and dia >= 22:
  print("Capricornio")
if mes == 1 and dia >= 21 or mes == 2 and dia <= 19:
  print("Aquario")
if mes == 2 and dia >= 20 or mes == 3 and dia <= 21:
  print("pisces")
if mes == 3 and dia >= 22 or mes == 4 and dia <= 20:
  print("aries")
if mes == 4 and dia >= 21 or mes == 5 and dia <= 21:
  print("tauro")
if mes == 5 and dia >= 22 or mes == 6 and dia <= 21:
  print("geminis")
if mes == 6 and dia >= 22 or mes == 7 and dia <= 23:
  print("cancer")
if mes == 7 and dia >= 24 or mes == 8 and dia <= 23:
  print("leo")
if mes == 8 and dia >= 24 or mes == 9 and dia <= 23:
  print("virgo")
if mes == 9 and dia >= 24 or mes == 10 and dia <= 23:
  print("libra")
if mes == 10 and dia >= 24 or mes == 11 and dia <= 22:
  print("escorpion")
if mes == 11 and dia >= 23 or mes == 12 and dia <= 21:
  print("sagitario") 