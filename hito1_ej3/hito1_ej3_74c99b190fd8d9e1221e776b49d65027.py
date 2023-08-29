#Aprobación de créditos
ingreso    = int(input("Ingreso salarial: "))
nacimiento = int(input("Año de nacimiento: "))
hijos      = int(input("Número de hijos: "))
banco      = int(input("Años de pertenencia al banco: "))
estado     = input("¿Estado civil? , digite S si es soltero, en caso de ser casado digitar C; ")
vivienda   = input("En que lugar vives?, digite U si es urbano, y si es rural digite R; ")

if (banco > 10 and hijos > 2):
    print("APROBADO")
    if (banco < 10 and hijos < 2) :
        print("RECHAZADO")

if (estado == "C" and hijos > 3 and nacimiento >= 1976 or nacimiento <= 1966):
        print("APROBADO")
        if (estado  == "S" and hijos < 3 and nacimiento <= 1976 or nacimiento >= 1966):
                print("RECHAZADO")

if (ingreso > 2500000 and estado == "S" and vivienda == "U"):
    print("APROBADO")
    if (ingreso < 2500000 and estado == "C" and vivienda == "R"):
           print("RECHAZADO")

if (ingreso > 3500000 and banco > 5):
    print("APROBADO")
    if(ingreso < 3500000 and banco < 5):
            print("RECHAZADO")

if (vivienda == "R" and estado == "C" and hijos < 2):
    print("APROBADO")
    if (vivienda == "R" and estado == "S" and hijos > 2):
        print("RECHAZADO")    