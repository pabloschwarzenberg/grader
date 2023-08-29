#Suma de los N primeros números
resultado = 0
n = int(input("Ingrese un n: "))

for i in range(0,n+1):
	resultado += i


print(resultado)