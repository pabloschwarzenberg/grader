#Aprobación de créditos
ingreso = int(input("Ingreso (Pesos): "))
a_nacimiento = int(input("Año de nacimiento: "))
n_hijos = int(input("Numero de hijos: "))
a_pertenencia = int(input("Años de pertenencia al banco "))
e_civil = input("Estado civil (""S"": soltero, ""C"", casado): ")
locacion = input("Si vive en campo o cuidad (""U"": urbano, ""R"": rural): ")

if a_pertenencia > 10 and n_hijos >= 2:
    print("APROBADO")
    exit()
if e_civil == "C" and n_hijos > 3 and (2020 - a_nacimiento <= 55 and 2020 - a_nacimiento >= 45):
    print("APROBADO")
    exit()
if ingreso > 2500000 and e_civil == "S" and locacion == "U":
    print("APROBADO")
    exit()
if ingreso > 3500000 and a_pertenencia > 5:
    print("APROBADO")
    exit()
if locacion == "R" and e_civil == "C" and n_hijos < 2:
    print("APROBADO")
    exit()
print("RECHAZADO")      
