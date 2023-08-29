#Contestador de celular
telefono =  input('Ingrese numero de telefono:' )
hora = int(input('Ingrese la hora de llamada: '))
if hora >= 0 and hora <= 7:
    print('CONTESTAR')
elif hora >= 8 and hora <= 14 and int((telefono[5:8])) == 909:
    print ('CONTESTAR')
elif hora >= 17 and hora <=19 and int((telefono[5:8])) == 877:
    print ('CONTESTAR')
else:
    print ('NO CONTESTAR')      