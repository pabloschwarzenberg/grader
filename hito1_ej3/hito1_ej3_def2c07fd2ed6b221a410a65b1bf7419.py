#Aprobación de créditos
ingreso=int(input("Ingreso: "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
pertenencia=int(input("Años de pertenencia al banco: "))
civil=input("Estado civil: ")
lugar=input("Si vive en campo o ciudad: ")
i=0
edad=2020-nacimiento
if pertenencia>10 and hijos>=2:
    i=i+1
if civil=="C" and hijos>3 and 45<=edad<=55:
    i=i+1
if ingreso>2500000 and civil=="S" and lugar=="U":
    i=i+1
if ingreso>3500000 and pertenencia>5:
    i=i+1
if lugar=="R" and civil=="C" and hijos<2:
    i=i+1
if i>=1:
    print("APROBADO")
else:
    print("RECHAZADO")      