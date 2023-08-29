def numero_perfecto(numero):
 suma = 0
 for n in range(1,numero):
	 if (numero % (n) == 0):
	   suma += (n)
 if (numero == suma):
	 return True
 else:
   return False