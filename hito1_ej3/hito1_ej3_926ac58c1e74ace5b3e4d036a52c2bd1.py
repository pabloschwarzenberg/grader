#Aprobación de créditos
ingreso = int(input("Ingreso en pesos: "))
año_nacimiento = int(input("Año de nacimiento: "))
numero_hijos = int(input("Número de hijos: "))
años_pertenencia = int(input("Años de pertenencia al banco: "))
edo_civil = str(input("Estado civil: "))
campo_ciudad = str(input("¿Vive en campo o ciudad?: "))

contador = 0

if años_pertenencia > 10 and numero_hijos >= 2:
	contador += 1

if edo_civil == "C" and numero_hijos > 3 and año_nacimiento >= 1967 and año_nacimiento <= 1977:
	contador += 1

if ingreso > 2500000 and edo_civil == "S" and campo_ciudad == "U":
	contador += 1

if ingreso > 3500000 and años_pertenencia > 5:
	contador += 1

if campo_ciudad == "R" and edo_civil == "C" and numero_hijos < 2:
	contador += 1

if contador >= 1:
	print("APROBADO")
else:
	print("RECHAZADO")      