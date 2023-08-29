def encontrar_todas(cadena, subcadena):
	posiciones = []
	posicion = 0
	
	while posicion != -1:
		posicion = cadena.find(subcadena,posicion)
		if posicion != -1:
			posiciones.append(posicion)
			posicion += 1

	return posiciones


cadena = 'mi mama me mima'
subcadena = 'ma'

posiciones = encontrar_todas(cadena, subcadena)

print('Posiciones:', posiciones)  