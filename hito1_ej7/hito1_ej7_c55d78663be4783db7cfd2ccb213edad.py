#Zodiaco
dia = int(input("ingrese el dia de nacimiento: "))
mes = int(input("ingrese el mes de nacimiento: "))

if mes == 1:
  if dia >= 1 and dia <= 20:
    print("capricornio")
  elif dia >= 21 and dia <= 31:
    print("acuario")
elif mes == 2:
  if dia >= 1 and dia <= 19:
    print("acuario")
  elif dia >=20 and dia <= 28:
    print("piscis")
elif mes == 3:
  if dia >= 1 and dia <= 21:
    print("piscis")
  elif dia >= 22 and dia <= 31:
    print("aries")
elif mes == 4:
  if dia >= 1 and dia <= 20:
    print("aries")
  elif dia >= 21 and dia <= 30:
    print("tauro")
elif mes == 5:
  if dia >= 1 and dia <= 21:
    print("tauro")
  elif dia >= 22 and dia <= 31:
    print("geminis")
elif mes == 6:
  if dia >= 1 and dia <= 21:
    print("geminis")
  elif dia >= 22 and dia <= 30:
    print("cancer")
elif mes == 7:
  if dia >= 1 and dia <= 23:
    print("cancer")
  elif dia >= 24 and dia <= 31:
    print("leo")
elif mes == 8:
  if dia >= 1 and dia <= 23:
    print("leo")
  elif dia >= 24 and dia <= 31:
    print("virgo")
elif mes == 9:
  if dia >= 1 and dia <= 23:
    print("virgo")
  elif dia >= 24 and dia <= 30:
    print("libra")
elif mes == 10:
  if dia >= 1 and dia <=23:
    print("libra")
  elif dia >= 24 and dia <= 31:
    print("escorpio")
elif mes == 11:
  if dia >= 1 and dia <= 22:
    print("escorpio")
  elif dia >= 23 and dia <= 30:
    print("sagitario")
elif mes == 12:
  if dia >= 1 and dia <=21:
    print("sagitario")
  elif dia >= 22 and dia <= 31:
    print("capricornio")     