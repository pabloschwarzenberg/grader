def cajero():
	
	saldo_cuenta=100000
	saldo_total=1000000
	saldo_cajero={
		20000: 20,
		10000: 40,
		5000: 40
	}
	
	intentos=0

	while True:
		
		usuario='10334151'
		clave='1803'
		print('')

		if usuario=='10334151' and clave=='1803':
			
			print('Inicio de sesion exitoso.')
			print('')
			print('BIENVENIDO')
			saldo_usuario=saldo_cuenta
			print('')
			break
			
		else:
			
			print('Usuario o clave invalidos.')
			intentos+=1
			print('')

			if intentos==3:
				
				print('TARJETA BLOQUEADA')
				return

	while True:
		
		monto=35000
		print('')

		if monto>saldo_usuario:
			
			print('Monto no permitido. Fondos insuficientes.')
			print('')
			
		elif monto>sum(k * v for k, v in saldo_cajero.items()):
			
			print('Monto no permitido. Cajero sin suficiente dinero.')
			print('')
			
		else:
			
			billetes_entregados={}
			saldo_usuario-=monto
			
			for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
				
				if monto>=billete and cantidad>0:
					
					cantidad_entregada=min(monto // billete, cantidad)
					billetes_entregados[billete]=cantidad_entregada
					monto-=billete * cantidad_entregada
					saldo_cajero[billete]-=cantidad_entregada

			print('Retiro exitoso.')
			print('')
			print('saldo cuenta=',saldo_usuario)
			print('')
			
			print('saldo cajero='+str(saldo_total-sum(saldo_cajero)))
			print('')
			print('suma biiletes=',sum(saldo_cajero))
			
			for billete, cantidad_entregada in billetes_entregados.items():
				
				print('billetes', billete, '=', cantidad_entregada)
				print('')

		opcion='N'
		print('')

		if opcion.upper()=='N':
			
			break

cajero()