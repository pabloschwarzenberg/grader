#Contestador de celular
num=int(input('numero: '))
hora=int(input('hora: '))
x=int(num/100000)
y=num%1000
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

print('resultado:', (respuesta))      