ingresos = int(input("Ingrese ingresos: "))
edad = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pertenencia = int(input("Ingrese cuantos años ha pertenecido al banco: "))
estado_civil = str(input("Ingrese estado civil (S: soltero, C, casado): "))
vivienda = str(input("Ingrese lugar de vivienda (U: urbano, R: rural): "))
if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and hijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingresos > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")