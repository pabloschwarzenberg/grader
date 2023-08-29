def suma_divisores(a):
	suma = 0
	es_primo = False
	for i in range(1, a):
		if a%i==0:
			suma += i
	if suma == 1:
		es_primo = True
	else:
		es_primo = False
	return suma, es_primo
	
print(suma_divisores(4))

           