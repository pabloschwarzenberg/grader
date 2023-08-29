#Aprobación de créditos
Ingreso = int(input("Ingrese sus ingresos (sin puntos o comas): "))
Nacimiento = int(input("Ingrese su año de nacimiento (ejemplo: 1970): "))
Num_hijos = int(input("Ingrese la cantidad de hijos que tenga: "))
Pertenencia_años = int(input("Ingrese la cantidad de años que ha pertenecido al banco: "))
Estado_civil = input("¿Usted es casado/a (C) o soltero/a(S)? ")
localidad = input("¿Usted vive en el campo(C) o en la ciudad(R)?")

if Pertenencia_años > 10 and Num_hijos >= 2:
    print("APROBADO")
elif Estado_civil == "C" and Num_hijos > 3 and 45 <(2022 - Nacimiento) < 55:
    print("APROBADO")
elif Ingreso > 2500000 and Estado_civil == "S" and localidad == "U":
    print("APROBADO")
elif Ingreso > 3500000 and Pertenencia_años > 5:
    print("APROBADO")
elif localidad == "R" and Estado_civil == "C" and Num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

