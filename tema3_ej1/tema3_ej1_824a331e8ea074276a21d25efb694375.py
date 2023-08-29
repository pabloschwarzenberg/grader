# completa el código de la función

def suma_divisores(a):
	suma = 0
	for i in range(1,a-1):
       
		if (a % (i) == 0):
        
			suma += (i)
          
	if suma == 1:
		return print("el número es primo")
	else:
		return print("el número no es primo")
print(suma_divisores(13) )  