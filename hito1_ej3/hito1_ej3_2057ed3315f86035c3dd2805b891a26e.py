#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso mensual (en pesos): "))
anonacimiento = int(input("Ingrese el año de nacimiento: "))
numerohijos = int(input("Ingrese el número de hijos: "))
anospertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estadocivil = input("Ingrese el estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese si vive en rural (R) o urbano (U): ")
# Verificar las reglas para decidir la aprobación del crédito
if anospertenencia > 10 and numerohijos >= 2:
    print("APROBADO")
elif estadocivil == "C" and numerohijos > 3 and 45 <= (2023 - anonacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estadocivil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anospertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estadocivil == "C" and numerohijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")