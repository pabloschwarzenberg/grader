#Ordenar tres números
fila = []

for i in range(0,3):
	numero = int(input("Ingrese numero: "))
	fila.append(numero)
	
fila.sort()

print(fila)