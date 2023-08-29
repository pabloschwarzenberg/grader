ingresos = int(input("Ingresos: "))
edad = int(input("Edad: "))
hijos = int(input("Cantidad de hijos: "))
años_banco = int(input("Años de pertenencia al banco: "))
estado_civil = input("¿Soltero o Casado? (responder solo usando S o C): ")
hogar = input("Vive en un lugar rural o urbano (responder solo usando R o U): ")

if años_banco >= 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and hijos >= 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingresos >= 2000000 and estado_civil == "S" and hogar == "U":
    print("APROBADO")
elif ingresos >= 3500000 and años_banco >= 5:
    print("APROBADO")
elif hogar == "R" and estado_civil == "C" and hijos <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")