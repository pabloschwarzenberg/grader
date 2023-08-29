#Ordenar tres números
#Ingreso de datos
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

menor = 0
medio = 0
mayor = 0

#Calculos
if (n1 < n2 and n1 < n3):
    menor = n1
    if (n2 > n3):
	    mayor = n2
	    medio = n3
    else:
	    mayor = n3
	    medio = n2
elif (n2 < n1 and n2 < n3):
    menor = n2
    if (n1 > n3):
	    mayor = n1
	    medio = n3
    else:
	    mayor = n3
	    medio = n1
else:
    menor=n3
    if (n1 > n2):
	    mayor = n1
	    medio = n2
    else:
	    mayor = n2
	    medio = n1

print("Los numeros ordenados de menor a mayor son:",menor,",",medio,",",mayor)