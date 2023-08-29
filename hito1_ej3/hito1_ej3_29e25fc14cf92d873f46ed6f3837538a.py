#Aprobación de créditos
IN = int(input("Ingreso (en pesos): "))
AN = int(input("Año de nacimiento: "))
NH = int(input("Número de hijos: "))
APB = int(input("Años de pertenencia al banco: "))
EC = str(input('Estado civil ("S": soltero, "C", casado): '))
VV = str(input('Si vive en campo o cuidad ("U": urbano, "R": rural): '))
EA = 2023 - AN

if (APB > 10 and NH >= 2) or (EC == "C" and NH >= 3 and (45 <= EA <= 55)) or (IN >= 250000 and EC == "S" and VV == "U") or (IN >= 350000 and APB > 5) or (VV == "R" and EC == "S" and NH <= 2):
    print("APROBADO")

else:
    print("RECHAZADO")