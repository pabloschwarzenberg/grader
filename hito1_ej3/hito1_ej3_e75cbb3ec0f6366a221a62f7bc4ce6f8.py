# Aprobación de créditos
ingreso = int(input('Ingresos: '))
nacimiento = int(input('Año de nacimiento: '))
Nhijos = int(input('N° de hijos: '))
pertenencia = int(input('Años de pertenencia al banco: '))
estado = input('Estado civil ("S": soltero, "C":casado): ')
ubicacion = input('lugar de vivienda ("U": Urbano, "R": Rural): ')
edad = (2022 - nacimiento)

if pertenencia > 10 and Nhijos >= 2:
    print("APROBADO")
elif (estado == "C") and (Nhijos > 3) and (45 <= edad <= 55):
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado == "C" and Nhijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")



