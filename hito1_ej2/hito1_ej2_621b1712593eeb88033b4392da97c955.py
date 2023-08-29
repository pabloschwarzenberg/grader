#Contestador de celular

n = int(input('ingrese su numero(8 digitos):'))
h = int(input('ingrese la hora(0-23):'))
pr = n//100000
ul = n%1000

if h<=7 and h>=0:
 print('contestar')
elif h>19:
 print('no contestar')
elif h<14 and ul==909:
 print('contestar')
elif h>=17 and h<=19 and pr!=877:
 print('contestar')
else:
 print('no contestar')