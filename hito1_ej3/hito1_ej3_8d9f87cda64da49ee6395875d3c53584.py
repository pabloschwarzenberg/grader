#Aprobación de créditos
i = int(input("Introduzca sus ingresos en pesos:"))
anac = int(input("Introduzca su año de nacimiento:"))
hijos = int(input("Introduzca número de hijos:"))
apertenencia = int(input("Introduzca años de pertenencia al banco:"))
ecivil = input("Introduzca su estado civil:")
print("S: soltero/a")
print("C: casado/a")
vive = input("Intruzca si vive en capo o ciudad:")
print("U: urbano")
print("R: rural")
edad = 2020 - anac
if ((apertenencia>10) and (hijos>=2)):
    print("APROBADO")
else:
    if ((ecivil=="C") and (hijos>3) and (45<=edad<=55)):
        print("APROBADO")
    else:
        if ((i>2500000) and (ecivil=="S") and (vive=="U")):
            print("APROBADO")
        else:
            if ((i>3500000) and (apertenencia>5)):
                print("APROBADO")
            else:
                if ((vive=="R") and (ecivil=="C") and (hijos<2)):
                    print("APROBADO")
                else:
                    print("RECHAZADO")