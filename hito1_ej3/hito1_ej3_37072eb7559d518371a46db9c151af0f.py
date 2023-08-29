#Aprobación de créditos

ING = int(input("ingrese sus ingresos: "))
AN = int(input("ingrese su año de nacimiento: "))
NH = int(input("ingrese numero de hijos: "))
AP = int(input("ingrese años de pertenencia al banco: "))
EC = str(input("ingrese estado civil, soltero(S) o casado(C): "))
V = str(input("ingrese lugar de vivienda, urbano (U) o rural(R): "))


#desarrollo

if AP > 10 and NH >= 2:
    print("APROBADO")

elif EC == "C" and NH > 3 and 1966 <= AN <= 1976:
    print("APROBADO")

elif ING > 2500000 and EC == "S" and V == "U":
    print("APROBADO")

elif V == "R" and EC == "C" and NH < 2:
    print("APROBADO")

elif ING > 3500000 and AP > 5:
    print("APROBADO")


else:
    print("RECHAZADO")
