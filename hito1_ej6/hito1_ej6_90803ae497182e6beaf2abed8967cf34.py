#Ordenar tres números
print("ingrese el primer número: ")
a=int(input())

print("ingrese el segundo número: ")
b=int(input())

print("ingrese el tercer número: ")
c=int(input())

if (a < b < c):
	menor = a

	if (b < c):
		medio = b
		mayor = c

	else:
		medio = c
		mayor = b

elif (b < a < c):
	menor = b

	if (a < c):
		medio = a
		mayor = c

	else:
		medio = c
		mayor = a

else:
	menor = c

	if (a < b):
		medio = a
		mayor = b

	else:
		medio = b
		mayor = a

	
#salida
		
print("El ORDEN DE MANERA ASCENDENTE ES:",menor , (","),medio , (","), mayor)