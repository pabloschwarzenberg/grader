#Aprobación de créditos
#Programa para acceder a creditos
ingreso= float(input("Indique su ingreso mensual: "))
año= float(input("Indique su año de naciemiento: "))
hijos= float(input("Indique el numero de hijos que tenga: "))
pertenencia= float(input("Indique los años de pertenencia al banco: "))
civil= input("Indique su estado civil, 'S' si es soltero, 'C' si es casado: ")
vivienda= input("Indique donde vive, 'R' si es en el campo, 'U' si es en ciudad: ")
if pertenencia > 10.0 and hijos >= 2.0:
    print("APROBADO")
elif civil.upper()== "C" and hijos > 3.0 and año in range (1967,1978):
    print("APROBADO")
elif ingreso > 2500000 and civil.upper()== "S" and vivienda.upper()== "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5.0:
    print("APROBADO")
elif vivienda.upper()== "R" and civil.upper()== "C" and hijos < 2.0:
    print("APROBADO")
else:
    print("RECHAZADO")    