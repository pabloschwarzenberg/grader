def amigos(a,b):
	acumular_a = 0
	for i in range(1,a):
		if a%i == 0:
			acumular_a += i
	acumular_b = 0
	for i in range(1,b):
		if b%i == 0:
			acumular_b += i
	if acumular_a == b and acumular_b == a:
		return True
	else:
		return False




           