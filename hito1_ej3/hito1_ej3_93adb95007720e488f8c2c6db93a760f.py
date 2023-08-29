ing = int(input("Ingrese su ingreso en pesos chilenos: "))
nac = int(input("Ingrese el año en el que nació: "))
hijos = int(input("Ingrese el número de hijos que tiene: "))
pert = int(input("Ingrese cuantos años ha estado en el banco: "))
civil = str(input("Ingrese si su estado civil, Casado (C) y Soltero (S): "))
hog = str(input(("Ingrese el lugar donde habita, Rural (R) y Urbano (U): ")))

if pert > 10 and hijos >= 2:
    print("APROBADO")
elif civil == ("C") and hijos < 3 and (2021 - nac) >=45 and (2021 - nac) <= 55:
    print("APROBADO")
elif ing >= 2500000 and civil == ("S") and hog == ("U"):
    print("APROBADO")
elif ing >= 3500000 and pert >= 5:
    print("APROBADO")
elif hog == ("R") and civil == ("C") and hijos > 2:
    print("APROBADO")
else:
    print("RECHAZADO")