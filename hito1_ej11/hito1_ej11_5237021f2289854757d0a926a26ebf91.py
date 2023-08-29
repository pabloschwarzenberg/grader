bill20 = 20000
bill10 = 10000
bill5 = 5000
caj20 = 20
caj10 = 40
caj5 = 40
scaj = (bill20*caj20)+(bill10*caj10)+(bill5*caj5) 
funca = 1
uid1 = 10334151
pass1 = 1803
monto1 = 100000
logscr = 1
attempt = 0
while funca == 1:
	if logscr == 1:
		logid = int(input('Ingresar numero de usuario: '))
		logpass = int(input('Ingrese clave: '))
		if (logid == uid1) and (logpass == pass1):
			logscr = 2
		else:
			attempt += 1
			print ('clave invalida')
			if attempt >= 3:
				print ('tarjeta bloqueada')
				funca = 0
	if logscr == 2:
		giro = int(input('Monto a retirar: '))
		if (giro > monto1) or (giro > scaj):
			print('monto no permitido')
		else:
			cbill20 = 0
			cbill10 = 0
			cbill5 = 0
			gtotal = 0
			while (gtotal != giro):
				if (giro % bill20 == 0):
					cbill20 += 1
					gtotal += bill20
				if (giro % bill10 == 0):
					cbill10 += 1
					gtotal += bill10
				if (giro % bill5 == 0):
					cbill5 += 1
					gtotal += bill5										
			monto1 -= giro
			scaj -= giro
			bremain20 = caj20 - cbill20 
			bremain10 = caj10 - cbill10
			bremain5 = caj5 - cbill5
			print('saldo cuenta=', monto1)
			print('saldo cajero=', scaj)
			print('billetes 20000=', cbill20)
			print('billetes 10000=', cbill10)
			print('billetes 5000=', cbill5)
			opc = input('presione N otra tecla: ')
			if (opc == 'N'):
				logscr = 2
			else:
				funca = 0
else:
	print('fin')