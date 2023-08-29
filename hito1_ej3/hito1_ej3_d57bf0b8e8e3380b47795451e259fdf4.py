ingreso = int(input("Ingreso"))
nacimiento = int(input("nacimiento"))
hijos = int(input("Hijos"))
pertenencia = int(input("años"))
estado_civil = input("estado civil S o C")
vivienda = input("U o R")

edad = 2022-nacimiento

if pertenencia > 10 and hijos >=2:
    print("APROBADO")
elif estado_civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso>2500000 and estado_civil=="S" and vivienda == "U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")