#Aprobación de créditos
ingreso = int(input("Ingreso: "))
nacimiento = int(input("Ano de nacimiento: "))
hijos = int(input("Hijos: "))
anosBanco = int(input("Anos banco: "))
estado = input("Estado civil (S, C): ")
vivienda = input("Vivienda (U, R): ")

anos = 2016 - nacimiento

if anosBanco > 10 and hijos >= 2:
	print("APROBADO")
elif estado == 'C' and hijos > 3 and 45 > anos > 55:
	print("APROBADO")
elif ingreso > 2500000 and estado == 'S' and vivienda == 'U':
	print("APROBADO")
elif ingreso > 3500000 and anosBanco > 5:
	print("APROBADO")
elif vivienda == 'R' and estado == 'C' and hijos < 2:
	print("APROBADO")
else:
	print("RECHAZADO")