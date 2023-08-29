#Aprobación de créditos
I = int(input("Ingreso en pesos: "))
A = int(input("Año de nacimiento: "))
NH = int(input("Numero de hijos: "))
AB = int(input("Año de pertenencia al banco: "))
EC = input("S:soltero, C:casado: ")
V = input("U:urbano, R:rural: ")

EDAD = (2021 - A)

if AB > 10 and NH >= 2:
    print("APROBADO")

elif EC == "C" and (NH > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")

elif I >= 2500000 and EC == "S" and V  == "U":
    print("APROBADO")

elif I == 3500000 and AB > 5:
    print("APROBADO")

elif V == "R" and EC == "C" and NH < 2:
    print("APROBADO")

else:
    print("RECHAZADO")
  