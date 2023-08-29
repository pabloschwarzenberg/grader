#Zodiaco
dia = int(input("Ingrese el día de nacimiento:"))
mes = int(input("Ingrese el mes de nacimiento:"))
if mes == 1:
  if dia <=20:
    signo = "capricornio"
  else:
    signo = "acuario"
if mes == 2:
  if dia <=18:
    signo = "acuario"
  else:
    signo = "piscis"
if mes == 3:
  if dia <=20:
    signo = "piscis"
  else:
    signo = "aries"
if mes == 4:
  if dia <=20:
    signo = "aries"
  else:
    signo = "tauro"
if mes == 5:
  if dia <=21:
    signo = "tauro"
  else:
    signo = "geminis"
if mes == 6:
  if dia <=21:
    signo = "geminis"
  else:
    signo = "cancer"
if mes == 7:
  if dia <=22:
    signo = "cancer"
  else:
    signo = "leo"
if mes == 8:
  if dia <=23:
    signo = "leo"
  else:
    signo = "virgo"
if mes == 9:
  if dia <=23:
    signo = "virgo"
  else:
    signo = "libra"
if mes == 10:
  if dia <=23:
    signo = "libra"
  else:
    signo = "escorpion"
if mes == 11:
  if dia <=22:
    signo = "escorpion"
  else:
    signo = "sagitario"
if mes == 12:
  if dia <=21:
    signo = "sagitario"
  else:
    signo = "capricornio"
print(signo)     