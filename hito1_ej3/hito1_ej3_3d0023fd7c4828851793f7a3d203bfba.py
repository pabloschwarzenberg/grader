#Aprobación de créditos
dinero = int(input("Ingreso en pesos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
años_banco = int(input("Año de pertenencia al banco: "))
estado_civil = input("S:soltero, C:casado: ")
lugar = input("U:urbano, R:rural: ")
EDAD = (2021 - nacimiento)
if años_banco > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and (hijos > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")
elif dinero >= 2500000 and estado_civil == "S" and lugar == "U":
    print("APROBADO")
elif dinero == 3500000 and años_banco > 5:
    print("APROBADO")
elif lugar == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")     