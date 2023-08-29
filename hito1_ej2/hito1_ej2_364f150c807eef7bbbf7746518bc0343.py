#Contestador de celular
nt=int(input('Numero telefonico: '))
h0=int(input('Hora del Dia: 0 hrs-23 hrs'))
nt1= int(str(nt) [-3:])
nt2= int(str(nt) [:3])
if h0 < 0 and h0 > 23:
  print('el numero ingresado es incorrecto')
elif h0 in(0,1,2,3,4,5,6,7):
  print('Resultado: CONTESTAR')
elif h0 in(8,9,10,11,12,13,14):
  if nt1 == 909:
    print('Resultado: CONTESTAR')
  else:
    print('Resultado: NO CONTESTAR')
elif h0 in(17,18,19):
  if nt2 == 877:
    print('Resultado: NO CONTESTAR')
  else:
    print('Resultado:CONTESTAR')
elif h0 in(20,21,22,23):
  print('Resultado: NO CONTESTAR')