Ingreso = int(input("Anote sus ingresos porfavor: "))
Año_de_nacimiento = int(input("Indique el año en el que nació: "))
Número_de_hijos = int(input("Indique el número de hijos: "))
Años_de_pertenencia = int(input("Indique los años de pertenencia al banco: "))
Estado_civil = input("Indique si esta casado(C) o soltero(S): ")
Campo_city = input("indique si vive en campo(R) o ciudad(U): ")
Edad = 2021 - Año_de_nacimiento

if (Años_de_pertenencia > 10) and (Número_de_hijos >= 2):
    print("APROBADO")
else:
        if (Estado_civil == 'C') and (Número_de_hijos > 3) and (45 <= Edad <=55):
            print("APROBADO")
        else:
            if (Ingreso >2500000) and (Estado_civil == 'S') and (Campo_city == 'U'):
                print("APROBADO")
            else:
                if (Ingreso > 3500000) and (Años_de_pertenencia > 5):
                    print("APROBADO")
                else:
                    if (Campo_city == 'R') and (Estado_civil == 'C') and (Número_de_hijos < 2):
                        print("APROBADO")
                    else:
                        print("RECHAZADO")

