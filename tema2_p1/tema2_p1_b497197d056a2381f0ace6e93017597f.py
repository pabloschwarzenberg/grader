# por favor escribe aquí tu función
def es_primo(nro): 
	if nro == 1:
		return False
	limite = nro + 2
	for x in range(2, limite):
		if nro % x == 0 and nro != x:
			return False
		elif x == (limite - 1) and nro % x != 0:
			return True      