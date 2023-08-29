#Aprobación de créditos
ingreso = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
años = int(input("Años en el banco: "))
estado = input("Estado civil (S:soltero, C:casado): ")
ciudad = input("Donde vive (U:urbano, R:rural")
if (años > 10 and hijos > 2) or (estado == "C" and hijos > 3 and años > 45 and años < 55) or (ingreso > 2500000 and estado == "S" and ciudad == "U") or (ingreso > 3500000 and años > 5) or (ciudad == "R" and estado == "C" and hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")