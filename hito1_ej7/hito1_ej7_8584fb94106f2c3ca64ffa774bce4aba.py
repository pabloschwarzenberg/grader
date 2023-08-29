#Zodiaco
print('**Mes y Dia de nacimiento**')
c = True
while c: #restriccion mes 1-12
    mes = int(input('Mes: '))
    if ((mes >= 1) and (mes <= 12)):
      c = False
    else:
      print ('Mes ingresado debe estar entre 1 y 12')
      
c = True
while c: #restriccion dias 1-31
    dia = int(input('Dia: '))
    if ((dia >= 1) and (dia <= 31)):
      c = False
    else:
      print ('Dia ingresado debe estar entre 1 y 31')

if (mes == 1):
  if (dia >= 20):
    print ('Signo Zodiacal: Aquarius')
  else:
    print ('Signo Zodiacal: Capricorn')
elif (mes == 2):
  if (dia >= 19):
    print ('Signo Zodiacal: Pisces')
  else:
    print ('Signo Zodiacal: Aquarius')
elif (mes == 3):
  if (dia >= 21):
    print ('Signo Zodiacal: Aries')
  else:
    print ('Signo Zodiacal: Pisces')
elif (mes == 4):
  if (dia >= 20):
    print ('Signo Zodiacal: Taurus')
  else:
    print ('Signo Zodiacal: Aries')
elif (mes == 5):
  if (dia >= 21):
    print ('Signo Zodiacal: Gemini')
  else:
    print ('Signo Zodiacal: Taurus')
elif (mes == 6):
  if (dia >= 21):
    print ('Signo Zodiacal: Cancer')
  else:
    print ('Signo Zodiacal: Gemini')
elif (mes == 7):
  if (dia >= 23):
    print ('Signo Zodiacal: Leo')
  else:
    print ('Signo Zodiacal: Cancer')
elif (mes == 8):
  if (dia >= 23):
    print ('Signo Zodiacal: Virgo')
  else:
    print ('Signo Zodiacal: Leo')
elif (mes == 9):
  if (dia >= 23):
    print ('Signo Zodiacal: Libra')
  else:
    print ('Signo Zodiacal: Virgo')
elif (mes == 10):
  if (dia >= 23):
    print ('Signo Zodiacal: Scorpio')
  else:
    print ('Signo Zodiacal: Libra')
elif (mes == 11):
  if (dia >= 22):
    print ('Signo Zodiacal: Sagittarius')
  else:
    print ('Signo Zodiacal: Scorpio')
elif (mes == 12):
  if (dia >= 22):
    print ('Signo Zodiacal: Capricorn')
  else:
    print ('Signo Zodiacal: Sagittarius')      