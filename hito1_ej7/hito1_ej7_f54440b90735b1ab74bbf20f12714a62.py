#Zodiaco
dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))

if dia > 31:
  dia = int(input("Dia invalido, reingrese su dia de nacimiento: "))
if mes > 12:
  mes = int(input("Mes invalido, reingrese su mes de nacimiento: "))

if mes == 12 or mes == 1:
  if mes == 12:
    if dia >= 22:
      print("su signo es Capricornio")
  elif mes == 1:
    if dia < 20:
      print("Su signo es Capricornio")


if mes == 1 or mes == 2:
  if mes == 1:
    if dia >= 20:
      print("Su signo es Acuario")
  elif mes == 2:
    if dia < 19:
      print("Su signo es Acuario")


if mes == 2 or mes == 3:
  if mes == 2:
    if dia >= 19:
      print("Su signo es Piscis")
  elif mes == 3:
    if dia < 21:
      print("Su signo es Piscis")


if mes == 3 or mes == 4:
  if mes == 3:
    if dia >= 21:
      print("Su signo es Aries")

  elif mes == 4:
    if dia < 20:
      print("Su signo es Aries")


if mes == 4 or mes == 5:
  if mes == 4:
    if dia >= 20:
      print("Su signo es Tauro")
  elif mes == 5:
    if dia < 21:
      print("Su signo es Tauro")


if mes == 5 or mes == 6:
  if mes == 5:
    if dia >= 21:
      print("Su signo es Geminis")
  elif mes == 6:
    if dia < 21:
      print("Su signo es Geminis")


if mes == 6 or mes == 7:
  if mes == 6:
    if dia >= 21:
      print("Su signo es Cancer")
  elif mes == 7:
    if dia < 23:
      print("Su signo es Cancer")


if mes == 7 or mes == 8:
  if mes == 7:
    if dia >= 23:
      print("Su signo es Leo")
  elif mes == 8:
    if dia < 23:
      print("Su signo es Leo")


if mes == 8 or mes == 9:
  if mes == 8:
    if dia >= 23:
      print("Su signo es Virgo")
  elif mes == 9:
    if dia < 23:
      print("Su signo es Virgo")


if mes == 9 or mes == 10:
  if mes == 9:
    if dia >= 23:
      print("Su signo es Libra")
  elif mes == 10:
    if dia <= 23:
      print("Su signo es Libra")


if mes == 10 or mes == 11:
  if mes == 10:
    if dia > 23:
      print("Su signo es Escorpio")
  elif mes == 11:
    if dia < 22:
      print("Su signo es Escorpio")


if mes == 11 or mes == 12:
  if mes == 11:
    if dia >= 23:
      print("Su signo es Sagitario")
  elif mes == 12:
    if dia < 22:
      print("Su signo es Sagitario")