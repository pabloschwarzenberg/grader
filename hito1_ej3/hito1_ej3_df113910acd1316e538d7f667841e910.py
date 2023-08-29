#Aprobación De Créditos
ing = int(input("Indique sus ingresos: "))
año_nacimiento = int(input("Ingrese su AÑO de nacimiento: "))
edad = (2022-año_nacimiento)
hijos = int(input("Indique su número de hijos: "))
años_pertenencia = int(input("Indique sus años de pertenencia en el banco: "))
estado_civil= input("Indique su estado civil S/C: ")
vivienda = input("Indique donde vive: \n U: Urbano \t R: Rural   :")

if años_pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and edad > 3 and edad >= 45  or edad <= 55:
    print("APROBADO")
elif ing > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ing > 3500000 and años_pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")