#Aprobación de créditos
Ingresos = int(input("Ingreso (en pesos)"))
Nacimiento = eval(input("Año de nacimiento"))
Hijos = int(input("Número de hijos"))
Banco = eval(input("Años de pertenencia al banco"))
Civil = str(input("Estado civil (S: soltero, C: casado)"))
DondeVive = str(input("Si vive en campo o cuidad (U: urbano, R: rural)"))
C = 1
S = 2
U = 3
R = 4
if Banco > 10 and Hijos >=2 :
    print("APROBADO")
else :
    if str(Civil) == 1 and Hijos > 3 and 2020 - Nacimiento >=45 and 2020 - Nacimiento <= 55 :
        print("APROBADO")
    else :
        if Ingresos > 2500000 and str(Civil) == 2 and str(DondeVive) == 3 :
            print("APROBADO")
        else :
            if Ingresos > 3500000 and Banco > 5 :
                print("APROBADO")
            else :
                if str(DondeVive) == 4 and str(Civil) == 1 and Hijos < 2 :
                    print("APROBADO")
                else :
                    print("NO APROBADO")