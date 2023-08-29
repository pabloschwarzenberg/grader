#Aprobación de créditos
ingresopesos = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
numerohijos = int(input("Numero de hijos: "))
BANCO = int(input("Años de pertenencia al banco: "))
estado= input("Estado civil (S: soltero, C: casado): ")
Vivienda = input("En que lugar vives? (U: Urbano, R: Rural): ")

if (BANCO > 10 and numerohijos > 2):
    print("APROBADO")
    if (BANCO < 10 and numerohijos < 2) :
        print("RECHAZADO")
if (estado == "C" and numerohijos > 3 and nacimiento >= 1976 or nacimiento <= 1966):
        print("APROBADO")
        if (estado  == "S" and numerohijos < 3 and nacimiento <= 1976 or nacimiento >= 1966):
                print("RECHAZADO")
if (ingresopesos > 2500000 and estado == "S" and Vivienda == "U"):
    print("APROBADO")
    if (ingresopesos < 2500000 and estado == "C" and Vivienda == "R"):
           print("RECHAZADO")
if (ingresopesos > 3500000 and BANCO > 5):
    print("APROBADO")
    if(ingresopesos < 3500000 and BANCO < 5):
            print("RECHAZADO")
if (Vivienda == "R" and estado == "C" and numerohijos < 2):
    print("APROBADO")
    if (Vivienda == "R" and estado == "S" and numerohijos > 2):
        print("RECHAZADO")      