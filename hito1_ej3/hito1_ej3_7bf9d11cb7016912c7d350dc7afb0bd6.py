q = int(input("Ingreso en pesos: "))
w = int(input("Año de nacimiento: "))
e = int(input("Numero de hijos: "))
t = int(input("Año de pertenencia al banco: "))
y = input("S:soltero, C:casado: ")
o = input("U:urbano, R:rural: ")

EDAD = (2021 - w)

if t > 10 and e >= 2:
    print("APROBADO")

elif y == "C" and (e > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")

elif q >= 2500000 and y == "S" and o  == "U":
    print("APROBADO")

elif q == 3500000 and t > 5:
    print("APROBADO")

elif o == "R" and y == "C" and e < 2:
    print("APROBADO")

else:
    print("RECHAZADO")