#Aprobación de créditos

ingre=int(input("Ingresos			: "))
nac=int(input("Año nacimineto	: "))
hijos=int(input("numero de hijos	: "))
año=int(input("Años pertenencia al Banco: "))
estado=input("Estado Civil		:")
domi=input("Estado Civil		:")

edad = 2021-año

if año > 10 and hijos >= 2:
	print("APROBADO")
elif estado == "C" and hijos > 3 and ((edad >=45) and (edad <=55)):
	print("APROBADO")
elif ingre > 2500000 and estado == "S" and domi == "U":
	print("APROBADO")
elif ingre > 3500000 and año > 5:
	print("APROBADO")
elif domi == "R" and estado == "C" and hijos < 2:
	print("APROBADO")
	
else:
	print("RECHAZADO")
	
