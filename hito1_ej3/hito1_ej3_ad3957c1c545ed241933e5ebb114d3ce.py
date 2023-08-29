#Aprobación de créditos
ingreso = int(input("Ingrese ingreso: "))
anoNacimiento = int(input("Año de nacimiento: "))
numeroHijos = int(input("Numero de hijos: "))
anoBanco = int(input("Ingrese años de pertenencia al banco: "))
estadoCivil = input("Estado civil ('S': Soltero, 'C': Casado ): ")
vive = input("Vive en campo o ciudad ('U': Urbano, 'R': Rural): ")

while (anoNacimiento > 0) and (anoBanco > 0):
    num = 2022 - anoNacimiento
    uwu = 2022 - anoBanco
    if anoBanco > 10 and numeroHijos >= 2:
        print("APROBADO")
        break
    elif (estadoCivil == "C") and (numeroHijos >= 3) and (45 < num < 55):
        print("APROBADO")
        break
    elif (ingreso > 250000) and (estadoCivil == "S") and (vive == "R"):
        print("APROBADO")
        break
    elif (ingreso > 350000) and (uwu > 5):
        print("APROBADO")
        break
    elif (vive == "U") and (estadoCivil == "C") and (numeroHijos < 2):
        print("APROBADO")
        break
    else:
        print("RECHAZADO")
        break