#Aprobación de créditos
A = int(input("Ingrese  los ingresos del postulante:"))
B = int(input("Ingrese el año de nacimiento del postulante:"))
C = int(input("Ingrese el numero de hijos que tiene el postulante:"))
D = int(input("Ingrese los años de pertenencia al banco del postulante:"))
E = str(input("Ingrese S si es soltero o C si es casado:"))
F = str(input("Ingrese U si vive en sector urbano o R si vive en sector rural:"))

Edad = (2020-B)
if D>10 and C>=2:
    print("APROBADO")
else:
    if E=="C" and C>3 and 45<=Edad<=55:
        print("APROBADO")
    else:
        if A>2500000 and E=="S" and F=="U":
            print("APROBADO")
        else:
            if A>3500000 and D>5:
                print("APROBADO")
            else:
                if F=="R" and E=="C" and C<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")      