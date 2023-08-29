#Aprobación de créditos

ingreso = int(input("Valor ingresos en pesos: "))
Año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
Número_de_hijos = int(input("Número de hijos: "))
Años_de_pertenencia_al_banco = int(input("Años que ha pertenecido al banco: "))
Esta_civil = input("Ingrese su estado civil (S/C): ")
Vive_campo_ciudad = input("Vive en (U/R): ")

if Años_de_pertenencia_al_banco > 10 and Número_de_hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    if Esta_civil == "C" and Número_de_hijos >= 3 and Año_de_nacimiento >= 1965 and Año_de_nacimiento <= 1975:
        print("APROBADO")
    else:
        print("RECHAZADO")
        if ingreso > 2500000 and Esta_civil == "S" and Vive_campo_ciudad == "U":
            print("APROBADO")
        else:
            print("RECHAZADO")
            if ingreso > 3500000 and Años_de_pertenencia_al_banco >= 5:
                print("APROBADO")
            else:
                print("RECHAZADO")
                if Vive_campo_ciudad == "R" and Esta_civil == "C" and Número_de_hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
    
              