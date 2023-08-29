#Aprobación de créditos
ingreso = int(input("Ingresos mensuales en pesos: "))
nacimiento = int(input("Ingrese su nacimiento: "))
hijos= int(input("Número de hijos: "))
banco = int(input("Años que lleva en el banco: "))
estadoCivil = str(input("Es (S)oltero o (C)asado?: "))
residencia = str(input("Zona donde vive, (U)rbana o (R)ural: "))
edad= 2020 - nacimiento


if banco > 10:
    if hijos >= 2:
        print("APROBADO")
    else:
        print("RECHAZADO")
if estadoCivil.capitalize() == "C":
    if hijos >= 3:
        if 45< edad <55:
            print("APROBADO")
if ingreso > 2500000:
    if estadoCivil.capitalize() == "S":
        if residencia == "U":
            print("APROBADO")
if ingreso > 3500000:
    if banco >= 5:
        print("APROBADO")
if residencia == "R":
    if estadoCivil.capitalize() == "C":
        if hijos < 2:
            print("APROBADO")
else:
    print("RECHAZADO")