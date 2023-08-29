#Aprobación de créditos
ingreso=int(input("Ingreso en pesos:"))
nacimiento=int(input("Año de nacimiento:"))
hijos=int(input("Numero de hijos:"))
pertenencia=int(input("años de pertenencia al banco:"))
estado_civil=input("Estado civil ('S': soltero, 'C', casado):")
ubicacion=input('Si vive en campo o cuidad ("U": urbano, "R": rural):')

def banco():
    if pertenencia>10 and hijos>1:
        print("APROBADO")

    elif estado_civil=="C" and hijos>3 and 55>(2016-nacimiento) and (2016-nacimiento)>45:
        print("APROBADO")

    elif ingreso>2500000 and estado_civil=="S" and ubicacion=="U":
        print("APROBADO")

    elif ingreso>3500000 and pertenencia>5:
        print("Aprobado")

    elif ubicacion=="R" and estado_civil=="C" and hijos<2:
        print("APROBADO")

    else:
        print("RECHAZADO")

banco()
    
