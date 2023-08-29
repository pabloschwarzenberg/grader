#Aprobación de créditos
I = int(input("Ingreso (en pesos):"))
Born = int(input("Año de nacimiento:"))
Hijos = int(input("Número de hijos:"))
Años = int(input("Años de pertenencia al banco:"))
Estado_Civil = input("Estado civil (S: soltero, C, casado):")
Localizacion = input("Si vive en campo o cuidad ("U": urbano, "R": rural):")
Edad = 2020 - Born

if Años>= 10 and Hijos >=2:
    print("APROBADO")
elif Estado_Civil == "C" and Hijos >= 3 and 45 <= Edad <= 55:
    print("APROBADO")
elif I > 2500000 and Estado_Civil == "S" and Localizacion == "U":
    print("APROBADO")
elif I > 3500000 and Años > 5:
    print("APROBADO")
elif Localizacion == "R" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      