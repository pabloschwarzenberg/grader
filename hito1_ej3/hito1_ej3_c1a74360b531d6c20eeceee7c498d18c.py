# Aprobación de créditos

ingreso = int(input("Ingreso: "))
año = int(input("año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
banco = int(input("Años de pertenencia al banco: "))
civil = str(input("Estado civil (S: Soltero / C: Casado): "))
lugar = str(input("lugar en donde vive (U: Urbano / R: Rural): "))

edad = 2023 - año

if banco >= 10 and hijos >= 2:
    print("APROBADO.")

elif civil == "C" and hijos >= 3 and 45 <= edad <= 55:
    print("APROBADO")

elif ingreso >= 2500000 and civil == "S" and lugar == "U":
    print("APROBADO")

elif ingreso >= 3500000 and banco >= 5:
    print("APROBADO")

elif lugar == "R" and civil == "C" and hijos <= 2:
    print("APROBADO")

else:
    print("RECHAZADO")
    