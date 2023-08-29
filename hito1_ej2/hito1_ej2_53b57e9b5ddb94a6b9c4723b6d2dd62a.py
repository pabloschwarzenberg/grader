#Contestador de celular
numTelefono=int(input('Ingrese su numero (8 digitos): '))
hora=int(input('Ingrese la hora de la llamada en 24HRS: '))
x=int(numTelefono/100000)
y=numTelefono%1000
if hora<=7:
  respuesta='CONTESTAR'
if 7<hora<14:
  respuesta='NO CONTESTAR'
if 7<hora<14 and y==909:
  respuesta='CONTESTAR'
if 14<=hora<17:
  respuesta='NO CONTESTAR'
if 17<=hora<=19:
  respuesta='CONTESTAR'
if 17<=hora<=19 and x==877:
  respuesta='NO CONTESTAR'
if 19<hora:
  respuesta='NO CONTESTAR'

print('>>>Resultado:', (respuesta))   