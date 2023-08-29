#Contestador de celular
tel=int(input('Ingrese numero telefonico: '))
if len(str(tel))==8:
  horas=int(input('Ingrese hora de la llamada: '))
  tele=str(tel)
  if 0>=horas<=7:
    print('Resultado: CONTESTAR')
  elif 7>horas<=14 and tele[-3:]=='909':
    print('Resultado: CONTESTAR')
  elif 17>=horas<=19 and tele[:-3]!='877':
    print('Resultado: CONTESTAR')
  else:
    print('Resultado: NO CONTESTAR')
else:
  print('numero ingresado es erroneo')