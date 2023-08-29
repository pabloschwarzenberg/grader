i=int(input("introduzca ingresos en pesos"))
anac=int(input("introduzca año nacimiento"))
hijos=int(input("hijos"))
apertenencia=int(input("años pertenencia"))
ecivil=input("estado civil")
print("S: soltero")
print("C: casado")
vive=input("ingrese urbano o rural")
print("U: urbano")
print("R: rural")
edad= 2020-anac
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
