#Contestador de celular
numero=int(input('ingrese el numero telefonico:'))
hora=int(input('ingrese la hora(0-23):'))
pr=numero//100000
ul=numero%1000

if hora<=7 and hora>=0:
 print ('contestar')
elif hora>19:
 print('no contestar')
elif hora<14 and ul==909:
 print('contestar')
elif hora>=17 and hora<=19 and pr!=877:
 print('contestar')
else:
 print('no contestar')