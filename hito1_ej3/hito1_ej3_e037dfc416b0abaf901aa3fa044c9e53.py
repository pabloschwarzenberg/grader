import datetime

ingreso = float(input("Ingreso: "))
nacimiento = int(input("Año nacimiento: "))
hijos = int(input("Cantidad de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil: (c)asado, (s)oltero): ")
zona = input("Zona: (U)rbano, (R)ural)")

anio_actual = datetime.date.today().year
edad = anio_actual - nacimiento

if pertenencia > 10 and hijos > 2:
    print("APROBADO")
elif estado_civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and zona == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif zona == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
