#Aprobación de créditos
#Aprobación de créditos


def Aprobacion_1(año_banco,num_hijos):
	if año_banco > 10 and num_hijos >=2:
		return "APROBADO"
	else:
		return "RECHAZADO"
		
def Aprobacion_2(estado_civil,num_hijos,año_nacimiento):
	edad = 2021 - año_nacimiento
	if estado_civil == "C" and num_hijos > 3 and edad > 45 and edad < 55:
		return "APROBADO"
	else:
		return "RECHAZADO" 

def Aprobacion_3(ingreso,estado_civil,campo_ciudad):
	if ingreso > 2500000 and estado_civil == "S" and campo_ciudad == "U":
		return "APROBADO"
	else:
		return "RECHAZADO"

def Aprobacion_4(ingreso,año_banco):
	if ingreso > 3500000 and año_banco > 5:
		return "APROBADO"
	else:
		return "RECHAZADO" 

def Aprobacion_5(campo_ciudad,estado_civil,num_hijos):
	if campo_ciudad == "R" and estado_civil == "C" and num_hijos < 2:
		return "APROBADO"
	else:
		return "RECHAZADO"


ingreso = int(input("Ingresa monto de ingreso: "))
ano_nacimiento = int(input("Ingresa año de nacimiento: "))
num_hijos = int(input("Ingresa numero de hijos: "))
ano_banco = int(input("Ingresa años en el banco:"))
estado_civil = input("Ingresa estado civil, (S) o (C): ")
campo_ciudad = input("Ingresa sector de recidencia, (U) o (R): ")
a1 = Aprobacion_1(ano_banco,num_hijos)
a2 = Aprobacion_2(estado_civil,num_hijos,ano_nacimiento)
a3 = Aprobacion_3(ingreso,estado_civil,campo_ciudad)
a4 = Aprobacion_4(ingreso,ano_banco)
a5 = Aprobacion_5(campo_ciudad,estado_civil,num_hijos)

if a1 == "APROBADO" or a2 == "APROBADO" or a3 == "APROBADO" or a4 == "APROBADO" or a5 == "APROBADO":
	print("APROBADO")
else:
	print("RECHAZADO")      