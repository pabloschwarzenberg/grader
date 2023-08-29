#aprobación de creditos
ingreso = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
Hijos = int(input("Numero de hijos: "))
BANCO = int(input("Años de pertenencia al banco: "))
Estado= input("Estado civil (S: soltero, C: casado): ")
Vivienda = input("En que lugar vives? (U: Urbano, R: Rural): ")

if (BANCO > 10 and Hijos > 2):
    print("APROBADO")
    if (BANCO < 10 and Hijos < 2) :
        print("RECHAZADO")

if (Estado == "C" and Hijos > 3 and nacimiento >= 1976 or nacimiento <= 1966):
        print("APROBADO")
        if (Estado  == "S" and Hijos < 3 and nacimiento <= 1976 or nacimiento >= 1966):
                print("RECHAZADO")

if (ingreso > 2500000 and Estado == "S" and Vivienda == "U"):
    print("APROBADO")
    if (ingreso < 2500000 and Estado == "C" and Vivienda == "R"):
           print("RECHAZADO")

if (ingreso > 3500000 and BANCO > 5):
    print("APROBADO")
    if(ingreso < 3500000 and BANCO < 5):
            print("RECHAZADO")

if (Vivienda == "R" and Estado == "C" and Hijos < 2):
    print("APROBADO")
    if (Vivienda == "R" and Estado == "S" and Hijos > 2):
        print("RECHAZADO")