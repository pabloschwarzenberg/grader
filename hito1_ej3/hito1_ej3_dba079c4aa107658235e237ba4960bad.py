#Aprobación de créditos
#Ingreso de datos
Ingreso = float(input("Cuales son sus ingresos?: "))
ano_nacimiento = float(input("En que año nacio?: "))
numero_de_hijos = float(input("Cuantos hijos tiene?: "))
anos_de_pertenencia = float(input("Cuantos años lleva con nosotros: "))
estado_civil = str(input("Cual es su estado civil?(soltero = S, casado = C): "))
residencia = str(input("Usted vive en la ciudad/urbano(U) o en el campo/rural(R)?: "))

#Rangos para saber si estas aprobado o no
aprobado = False
if anos_de_pertenencia >10 and numero_de_hijos >=2:
    aprobado = True
if estado_civil == "C" and numero_de_hijos > 3 and 45<=(2023 - ano_nacimiento)<=55:
    aprobado = True
if Ingreso > 2500000 and estado_civil == "S" and residencia == "U":
    aprobado = True
if Ingreso > 3500000 and anos_de_pertenencia > 5:
    aprobado = True
if residencia == "R" and estado_civil == "C" and numero_de_hijos < 2:
    aprobado = True

#imprimir datos
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")