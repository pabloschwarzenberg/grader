ingreso=eval(input("Monto de ingreso:"))
anio=eval(input("Ingrese su año de nacimiento:"))
nroHijos=eval(input("Cantidad de hijos:"))
anioBanco=eval(input("Años de perteneia en el Banco:"))
estadoC=input("Ingrese su estado civi, S soltero, C casado:")
vivienda=input("Donde vive Campo(R) o Ciudad(U)")
anio=anio-2021
if anioBanco>=10:
    if nroHijos>=2:
        print("APROBADO")
    else:
        print("RECHAZADO")
if estadoC=="C":
    if nroHijos>3:
        if (anio>=45 and anio<=55):
            print("APROBADO")
        else:
            print("RECHAZADO")
if ingreso>=2500000:
    if estadoC=="S":
        if vivienda=="U":
            print("APROBADO")
        else:
            print("RECHAZADO")
if ingreso>=3500000:
    if anioBanco>=5:
        print("APROBADO")
    else:
        print("RECHAZADO")
if vivienda=="R":
    if estadoC=="C":
        if nroHijos<2:
            print("APROBADO")
        else:
            print("RECHAZADO")