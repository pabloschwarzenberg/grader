#Ordenar tres números

n1=eval(input("Ingrese primer numero:  "))
n2=eval(input("Ingrese Segundo numero:  "))
n3=eval(input("Ingrese tercer numero:  "))

primero=0
segundo=0
tercero=0

if (n1<=n2) and (n1<=n3):
	primero=n1
	if n2<=n3:
		segundo=n2
		tercero=n3
	else:
		segundo=n3
		tercero=n2
elif (n2<=n1) and (n2<=n3):
	primero=n2
	if n1<=n3:
		segundo=n1
		tercero=n3
	else:
		segundo=n3
		tercero=n1
else:
	primero=n3
	if n1<=n2:
		segundo=n1
		tercero=n2
	else:
		segundo=n2
		tercero=n1
		
print(primero,"," ,segundo,",", tercero)
