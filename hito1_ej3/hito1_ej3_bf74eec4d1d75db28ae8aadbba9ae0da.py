#Aprobación de créditos
Ingreso = input("Ingrese su ingreso mensual: ")
AnioDeNacimiento = input("Ingrese su año de nacimiento: ")
NumeroDeHijos = input("Número de hijos: ")
AniosDepertenencia_al_banco = input("Años de pertenencia al banco: ")
EstadoCivil = input("Estado civil (S/C): ")
ZonaDeVivienda = input("Vive en zona urbana o rural(U/R): ")
anioactual = 2020
Edad = int(anioactual) - int(AnioDeNacimiento)

if int(AniosDepertenencia_al_banco) > 10 and int(NumeroDeHijos) >= 2:
        print("APROBADO")
        if int(AniosDepertenencia_al_banco) < 10:
                print("RECHAZADO")
elif EstadoCivil == "C" and int(NumeroDeHijos) > 3 and 45 < int(Edad) < 55:
        print("APROBADO ")
        if 45 == int(Edad) or 55 == int(Edad):
                print("RECHAZADO")
elif int(Ingreso) > 2500000 and EstadoCivil == "S" and ZonaDeVivienda == "U":
        print("APROBADO ")
        if int(Ingreso) < 2500000 or EstadoCivil != "S" or ZonaDeVivienda != "U":
                print("RECHAZADO")
elif int(Ingreso) > 3500000 and int(AniosDepertenencia_al_banco) > 5:
        print("APROBADO")
        if int(Ingreso) < 3500000 or int(AniosDepertenencia_al_banco) < 5:
                print("RECHAZADO")
elif ZonaDeVivienda == "R" and int(NumeroDeHijos) < 3 and EstadoCivil == "C":
        print("APROBADO")
        if ZonaDeVivienda != "R" or int(NumeroDeHijos) > 3:
                print("RECHAZADO")