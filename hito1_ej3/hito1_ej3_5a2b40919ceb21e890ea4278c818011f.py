#Aprobación de créditos
ingresos = int(input("Ingresos en pesos: "))
nacimiento = int(input("Año de nacimiento: "))
n_hijos = int(input("Numero de hijos: "))
ap_banco = int(input("Años de pertenencia al banco: "))
e_civil = input("Estado civil (s = soltero, c = casado): ")
localidad = input("Que zona vive (u = urbana, r = rural): ")

edad = 2023 - nacimiento

if ap_banco > 10 and n_hijos >= 2:
    print("APROBADO")
elif e_civil == "C" and n_hijos > 3 and edad >= 45 and edad <=55:
    print("APROBADO")
elif ingresos > 2500000 and e_civil == "S" and localidad == "U":
    print("APROBADO")
elif ingresos > 3500000 and ap_banco > 5:
    print("APROBADO")
elif localidad == "R" and e_civil == "C" and n_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")