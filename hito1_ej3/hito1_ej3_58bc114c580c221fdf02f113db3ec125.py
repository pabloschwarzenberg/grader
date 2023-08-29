#Aprobación de créditos
Z = int(input("Ingreso en pesos: "))
Y = int(input("Año de nacimiento: "))
X = int(input("Numero de hijos: "))
W = int(input("Año de pertenencia al banco: "))
V = input("S:soltero, C:casado: ")
U = input("U:urbano, R:rural: ")

EDAD = (2021 - Y)

if W > 10 and W >= 2:
    print("APROBADO")

elif V == "C" and (X > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")

elif Z >= 2500000 and V == "S" and U  == "U":
    print("APROBADO")

elif Z == 3500000 and W > 5:
    print("APROBADO")

elif V == "R" and V == "C" and Z < 2:
    print("APROBADO")

else:
    print("RECHAZADO")      