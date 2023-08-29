#Ordenar tres números
numero_1=int(input("Ingrese el primer numero: "))
numero_2=int(input("Ingrese el segundo numero: "))
numero_3=int(input("Ingrese el tercer numero: "))

if numero_1<numero_2 and numero_1<numero_3:
	if numero_2<numero_3:
		print(str(numero_1)+", "+ str(numero_2)+ ", "+ str(numero_3))
	else:
		print(str(numero_1)+", "+ str(numero_3)+ ", "+ str(numero_2))

if numero_2<numero_1 and numero_2<numero_3:
	if numero_1<numero_3:
		print(str(numero_2)+", "+ str(numero_1)+ ", "+ str(numero_3))
	else:
		print(str(numero_2)+", "+ str(numero_3)+ ", "+ str(numero_1))

if numero_3<numero_1 and numero_3<numero_2:
	if numero_1<numero_2:
		print(str(numero_3)+", "+ str(numero_1)+ ", "+ str(numero_2))
	else:
		print(str(numero_3)+", "+ str(numero_2)+ ", "+ str(numero_1))    