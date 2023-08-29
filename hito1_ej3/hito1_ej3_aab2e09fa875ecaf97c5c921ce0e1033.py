ingresos = int(input("Ingrese sus ingresos en CLP ", ))
edad = int(input("Ingrese su Año de nacimiento ", ))
hijos = int(input("Ingrese cuantos hijos e hijas tiene ", ))
anos = int(input("Ingrese sus años de pertenencia al banco ", ))
Estado_Civil = (input("Ingrese su estado civil ", ))
if Estado_Civil=="C" or Estado_Civil=="Casado" or Estado_Civil=="casado" or Estado_Civil=="c":
    Estado_Civil=1
else: Estado_Civil=0
Vivienda = (input("Si usted vive en la ciudad ingrese una U, si vive en el campo ingrese una R ", ))
if Vivienda=="U":
    Vivienda=1
else:Vivienda=0

if anos>10 and hijos>=2:
    print("APROBADO")
else:
    if Estado_Civil==1 and hijos>3 and edad>=45 and edad<=55:
        print("APROBADO")
    else:
        if ingresos>2500000 and Estado_Civil==1 and Vivienda==1:
            print("APROBADO")
        else:
            if ingresos>3500000 and anos>5:
                print("APROBADO")
            else:
                if Vivienda==0 and Estado_Civil==1 and hijos<3:
                    print("APROBADO")
                else: print("RECHAZADO")
