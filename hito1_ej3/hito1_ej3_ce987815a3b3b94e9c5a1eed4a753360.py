#Aprobación de créditos

ingreso = input("Ingrese su ingreso mensual: ")
añoNacimiento = input("Ingrese su año de nacimiento: ")
nHijos = input("Número de hijos: ")
aPertenenciaBanco = input("Años de pertenencia al banco: ")
eCivil = input("Estado civil (S/C): ")
zonaVivienda = input("Vive en zona urbana o rural(U/R): ")
añoActual = 2020
edad = int(añoActual) - int(añoNacimiento)

if int(aPertenenciaBanco) > 10 and int(nHijos) >= 2:
        print("APROBADO")
        if int(aPertenenciaBanco) < 10:
                print("RECHAZADO")
elif eCivil == "C" and int(nHijos) > 3 and 45 < int(edad) < 55:
        print("APROBADO!")
        if 45 == int(edad) or 55 == int(edad):
                print("RECHAZADO!")
elif int(ingreso) > 2500000 and eCivil == "S" and zonaVivienda == "U":
        print("APROBADO!")
        if int(ingreso) < 2500000 or eCivil != "S" or zonaVivienda != "U":
                print("RECHAZADO!")
elif int(ingreso) > 3500000 and int(aPertenenciaBanco) > 5:
        print("APROBADO!")
        if int(ingreso) < 3500000 or int(aPertenenciaBanco) < 5:
                print("RECHAZADO!")
elif zonaVivienda == "R" and int(nHijos) < 3 and eCivil == "C":
        print("APROBADO!")
        if zonaVivienda != "R" or int(nHijos) > 3:
                print("RECHAZADO!")     