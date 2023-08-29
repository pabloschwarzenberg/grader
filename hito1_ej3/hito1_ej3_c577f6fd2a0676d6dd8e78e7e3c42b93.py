#Aprobación de créditos
ingreso = int(input("Ingreso: "))
ano_nacimiento = int(input("Año de año nacimiento: "))
numero_hijos = int(input("Cantidad de hijos: "))
antiguedad_banco = int(input("Años de pertenencia al banco: "))
estado_civil = input("S: soltero, C: casado: ")
campo_cuidad = input("U: urbano, R: rural: ")

edad= ano_nacimiento-2020

if antiguedad_banco > 10 and numero_hijos >= 2:
	print("APROBADO")

if (estado_civil == "C" or estado_civil == "c") and numero_hijos > 3 and 45 <= edad >= 55:
	print("APROBADO")

if ingreso > 2500000 and (estado_civil == "S" or estado_civil == "s") and (campo_cuidad == "U" or campo_cuidad == "u"):
	print("APROBADO")

if ingreso > 3500000 and antiguedad_banco > 5:
	print("APROBADO")

if (campo_cuidad == "R" or campo_cuidad == "r") and (estado_civil == "C" or estado_civil == "c") and numero_hijos < 2:
	print("APROBADO")

else:
	print("Rechazado")