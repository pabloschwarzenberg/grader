#Contestador de celular
nrotel=int(input('Ingrese un numero telefonico de 8 cifras sin separacion: '))
tele=str(nrotel)
	
if len(tele)==8:

	a=int(tele[7:8]) 
	b=int(tele[6:7])
	c=int(tele[5:6]) 
	d=int(tele[4:5])
	e=int(tele[3:4])
	f=int(tele[2:3])
	g=int(tele[1:2])
	h=int(tele[0:1])
		
	print('')
		
	hora=int(input('Ingrese la hora de llamada desde las 0 a las 23 sin minutos: '))
		
	if hora>=0 and hora<=7:
		print('')
		print('CONTESTAR')
		print('')
		
	elif hora>=8 and hora<=13 and c==9 and b==0 and a==9:
		print('')
		print('CONTESTAR')
		print('')
		
	elif hora>=17 and hora<=19:
			
		if h==8 and g==7 and f==7:
			print('')
			print('NO CONTESTAR')
			print('')
		
		else:
			print('')
			print('CONTESTAR')
			print('')
			
	else:
		print('')
		print('NO CONTESTAR')
		print('')

else:
	print('')
	print('INGRESE UN NUMERO VALIDO')
	print('') 