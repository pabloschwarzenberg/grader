#Aprobación de créditos
S=1
C=2
U=3
R=4

ingreso=eval(input("Ingrese el monto: "))
fecha=eval(input("Ingrese año de nacimiento: "))
hijos=eval(input("Ingrese el numero de hijos: "))
anosbanco=eval(input("Ingrese años de pertenencia al banco: "))
estado=eval(input("Ingrese su estado civil S/C : "))
hogar=eval(input("Ingrese donde vive U/R: "))



edad=2020-fecha

if hijos >= 2 and anosbanco > 10:
    print("APROBADO")
else:
    print("RECHAZADO")

    if estado == 2 and hijos > 3 and edad > 45 < 55:
        print("APROBADO")
    else:
        print("RECHAZADO")
    if ingreso > 2500000 and estado == 1 and hogar == 3:
        print("APROADO")
    else:
        print("RECHAZADO")
    if ingreso > 3500000 and anosbanco < 5:
        print("APROBADO")
    else:
        print("RECHAZADO")
    if hogar == 4 and estado == 2 and hijos < 2 > 0:
        print("APROBADO")
    else:
        print("RECHAZADO")

