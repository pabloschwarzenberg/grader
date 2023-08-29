#Aprobación de créditos
ingreso=int(input("Ingrese sus ingresos: "))
fechan=int(input("Ingrese su año de nacimiento: "))
nhijos=int(input("Ingrese el numero de hijos: "))
apert=int(input("Ingrese los años de pertenencia al banco: "))
estadoc=input("Estado civil: S, Soltero, C casado: ")
campociudad=input("Si vive en campo o cuidad ("U": urbano, "R": rural)")
edad=2022-fechan
if apert>10 and nhijos<=2:
    print("APROBADO.")
if estadoc=="c" or estadoc=="C" and nhijos>3 and edad>=45 or edad<=55:
    print("APROBADO.")
if ingreso>2500000 and estadoc=="S" and campociudad=="U":
    print("APROBADO.")
if ingreso>3500000 and apert>5:
    print("APROBADO.")
if campociudad=="R" and estadoc=="C" and nhijos<2:
    print("APROBADO.")
