a = float(input("Ingrese sus ingresos en pesos:"))
b = int(input("Ingrese año de nacimiento:"))
c = int(input("Ingrese cantidad de hijos:"))
d = int(input("Ingrese años de pertenencia al banco:"))
e = str(input("Ingrese estado civil, S si esta soltero, C si esta casado:"))
f = (input("Ingrese si vive en urbano (U) o rural (R):"))
if d > 10 and c >= 2:
    print("APROBADO")
elif e == "C" and c > 3 and  1963< b <1973 :
    print("APROBADO")

elif a > 2500000 and e == "S" and f == "U":
    print("APROBADO")

elif a > 3500000 and d > 5:
    print("APROVADO")

elif f == "R" and e == "C" and c < 2:
    print("APROBADO")

else:
    print("RECHAZADO")

