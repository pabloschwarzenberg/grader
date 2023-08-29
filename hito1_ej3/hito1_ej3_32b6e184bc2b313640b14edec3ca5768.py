#Aprobación de créditos
#INPUT DE DATOS

ingreso=int(input("Ingresos en pesos: "))
ano_nacimiento=int(input("Año de nacimiento: "))
edad=2018-ano_nacimiento
num_hijos=int(input("Número de hijos: "))
anos_en_banco=int(input("Años de pertenencia al banco: "))
estado_civil=input("'C' si estás casado ; 'S' si estás soltero: ")
vivienda= input("'U' si vive en ciudad ; 'R' si vive en campo: ")

#DECISIÓN DE APROBACIÓN: con una de ellas que se cumpla, se aprueba el crédito:
if (anos_en_banco>10 and num_hijos>=2) or (estado_civil=="C" and num_hijos>3 and 45<edad<55) or (ingreso> 2500000 and estado_civil=="S" and vivienda=="U") or (ingreso>3500000 and anos_en_banco>5) or (vivienda=="R" and estado_civil=="C" and num_hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")