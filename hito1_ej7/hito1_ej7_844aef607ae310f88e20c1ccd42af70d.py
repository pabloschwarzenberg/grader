#Zodiaco
print('Ingrese los siguientes datos: ')
dia = eval(input('Ingrese el dia de su cumpleaños: '))
mes = eval(input('Ingrese el mes de su cumpleaños: '))

if (mes == 3 and dia >=21) or (dia<=20 and mes == 4):
  print('Signo: Aries')
elif (mes == 4 and dia>=20) or (dia<=21 and mes == 5):
  print('Signo: Tauro')
elif (mes == 5 and dia>=21) or (dia<=21 and mes == 6):
  print('Signo: Geminis')
elif (mes == 6 and dia>=21) or (dia<=23 and mes == 7):
  print('Signo: Cancer')
elif (mes == 7 and dia>=23) or (dia<=23 and mes == 8):
  print('Signo: Leo')
elif (mes == 8 and dia>=23) or (dia<=23 and mes == 9):
  print('Signo: Virgo')
elif (mes == 9 and dia>=23) or (dia<=23 and mes == 10):
  print('Signo: Libra')
elif (mes == 10 and dia>=23) or (dia<=22 and mes == 11):
  print('Signo: Escorpio')
elif (mes == 11 and dia>=22) or (dia<=22 and mes == 12):
  print('Signo: Sagitario')
elif (mes == 12 and dia>=22) or (dia<=20 and mes == 1):
  print('Signo: Capricornio')
elif (mes == 1 and dia>=20) or (dia<=19 and mes == 2):
  print('Signo: Acuario')
else:
  print('Signo: Piscis')
