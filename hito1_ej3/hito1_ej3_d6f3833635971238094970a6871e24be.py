I = float(input("Ingreso :"))
ADN = float(input("Año de nacimiento (Si aún no ha cumplido años, restele a su edad 1 año y ingreselo) :"))
NH = float(input("Número de hijos :"))
CT = int(input("Años de pertenencia al banco :"))
EC = input("Estado civil(S: soltero, C:casado)")
COP = input("Si vive en campo o cuidad (U: urbano, R: rural)")
valor1 = 2020
valor2 = valor1 - ADN

if CT >= 10 and NH >= 2:
    print("APROBADO")
else:
    if EC == "C" and NH > 3 and 45 < valor2 < 55:
        print("APROBADO")
    else:
        if 2500000 < I and EC == "S" and COP == "U":
            print("APROBADO")
        else:
            if 3500000 < I and 5 < CT:
                print("APROBADO")
            else:
                if COP == "R" and EC == "C" and NH < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")