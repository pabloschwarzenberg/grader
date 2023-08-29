#Entrada

I = int(input("Ingrese su ingreso en pesos: "))
N = int(input("Ingrese su ano de nacimiento: "))
NH = int(input("Ingrese el numero de hijos que tiene: "))
PB = int(input("Ingrese los anos pertenecientes al banco: "))
EC = input("Ingrese su estado civil, si esta casado C y si se encuentra soltero S: ")
RA = input("Ingrese si vive en un sector urbano U o en un sector rural R: ")

EDAD = (2021 - N)

#procesamiento

if PB >= 10 and NH >= 2:
    print("APROBADO")

elif EC == "C" and NH > 3 and EDAD > 45 and EDAD < 55:
    print("APROBADO")

elif I > 2500000 and EC == "S" and RA == "U":
    print("APROBADO")

elif I > 3500000 and PB > 5:
    print("APROBADO")

elif RA == "R" and EC == "C" and NH < 2:
    print("APROBADO")

else:
    print("RECHAZADO")