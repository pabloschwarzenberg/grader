#Zodiaco
continua = True
while True:
 dia = int(input('ingrese dia de cumpleaños: '))
 if dia > 31 or dia < 1:
    print('Error dia ingresado no existe')
    break
 mes = int(input('ingrse mes de cumpleaños: '))
 if mes > 12 or mes < 1:
    print('Error mes no existe')
    break
 else:
  if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1) :
    print('signo = Capricornio')
    break
  elif (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2) :
    print('signo = Acuario')
    break
  elif (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3) :
    print('signo = Piscis')
    break
  elif (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4) :
    print('signo = Aries')
    break
  elif (dia >= 21 and mes == 4) or (dia <= 21 and mes == 5) :
    print('signo = Tauro')
    break
  elif (dia >= 22 and mes == 5) or (dia <= 21 and mes == 6) :
    print('signo = Geminis')
    break
  elif (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7) :
    print('signo = Cancer')
    break
  elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8) :
    print('signo = Leo')
    break
  elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9) :
    print('signo = Virgo')
    break
  elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10) :
    print('signo = Libra')
    break
  elif (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11) :
    print('signo = Escorpion')
    break
  elif (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12) :
    print('signo = Sagitario')
    break
else:
    print('Datos ingresados son erroneos')      