#Suma de los N primeros números
n=int(input("Ingresa un numero natural :"))
suma=0
if (n <= 0):
  print("ingreso un numero menor a 1 por lo que no pertenece a los Naturales")

else:
	suma=(n*(n+1))/2
	print("la suma d los numeros naturales es : ", suma)