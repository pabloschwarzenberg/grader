# completa el código de la función
# completa el código de la función
def suma_divisores(a):
	suma = 0
	primos = 0
	for i in range(1,a):
 		if a % i == 0:
 			primos = primos + i
 			suma = suma + i
      		
	if primos == 1:
		return 1, True
	else:
		return suma, False



