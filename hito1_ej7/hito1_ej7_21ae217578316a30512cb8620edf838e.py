#Zodiaco
dia = int(input())
mes = int(input())
if mes== 1:
  if dia<20:
    print('CAPRICORNIO')
  else:
    print('ACUARIO')
elif mes == 2:
  if dia<19:
    print('ACUARIO')
  else:
    print('PICIS')
elif mes== 3:
  if dia<21:
    print('PICIS')
  else:
    print('ARIES')
elif mes == 4:
  if dia<20:
    print('ARIES')
  else:
    print('TAURO')
elif mes == 5:
  if dia<21:
    print('TAURO')
  else:
    print('GEMINIS')
elif mes == 6:
  if dia<23:
    print('GEMINIS')
  else:
    print('CANCER')
elif mes == 7:
  if dia<23:
    print('CANCER')
  else:
    print('LEO')
elif mes == 8:
  if dia<23:
    print('LEO')
  else:
    print('VIRGO')
elif mes == 9:
  if dia<23:
    print('VIRGO')
  else:
    print('LIBRA')
elif mes == 10:
  if dia<23:
    print('LIBRA')
  else:
    print('ESCORPIO')
elif mes == 11:
  if dia<23:
    print('ESCORPIO')
  else:
    print('SAGITARIO')
else:
  if dia<22:
    print('SAGITARIO')
  else:
    print('CAPRICORNIO')