#Aprobación de créditos
ingreso = int(input("Ingreso (en pesos)"))
a_nacimiento = int(input("Año de nacimiento"))
edad = 2022 - a_nacimiento
num_hijos = int(input("Número de hijos"))
a_pertenencia = int(input("Años de pertenencia al banco"))
e_civil = str(input("Estado civil ('S': soltero, 'C', casado)"))
zona = str(input("Si vive en campo o cuidad ("U": urbano, "R": rural)"))

if a_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif e_civil == "C" and num_hijos > 3 and edad in range(45, 56):
    print("APROBADO")
elif ingreso > 2500000 and e_civil == "S" and zona == "U":
    print("APROBADO")
elif ingreso > 3500000 and a_pertenencia > 5:
    print("APROBADO")
elif zona == "R" and  e_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO ")