ing = int(input("Ingresos: "))
An = int(input("Año de nacimiento: "))
NH = int(input("Numero de hijos: "))
AP = int(input("Años de pertenencia al banco: "))
EC = input("Estado civil(S:soltero,C:casado): ")
UR = input("Vive en campo o ciudad(U:urbano,R:rural): ")
Edad = 2020 - An

if AP > 10 and NH >= 2:
    print("APROBADO")
elif EC == "C" and NH > 3 and Edad >= 45 and Edad <= 55:
    print("APROBADO")
elif ing > 2500000 and NH == "S" and UR == "U":
    print("APROBADO")
elif ing > 3500000 and AP > 5:
    print("APROBADO")
elif UR == "R" and EC == "C" and NH < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      