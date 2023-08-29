ingreso = eval(input("Ingresos: "))
nacimiento = eval(input("Año de nacimiento: "))
hijos = eval(input("Número de hijos: "))
banco = eval(input("Años de pertenencia al banco: "))
civil = int(input("Estado civil: "))
vivienda = int(input("Si vive en campo o ciudad: "))
if(civil == c and vivienda == r and hijos<2):
    print("APROBADO")
else:
    print("REPROBADO")
if(banco>=10 and hijos>=2):
    print("APROBADO")
else:
    print("REPROBADO")
if(banco>=5 and ingreso>= 3500000):
    print("APROBADO")
else:
    print("REPROBADO")