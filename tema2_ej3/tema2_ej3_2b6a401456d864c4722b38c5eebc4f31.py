import math
def numero_perfecto(Num):
	cont = 0
	for i in range(1,Num):
		if Num % i == 0:
			cont = cont + i
	if cont == Num:
		return True
	else:
		return False