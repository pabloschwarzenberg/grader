#Aprobación de créditos
ing=int(input("Su ingreso es de: "))
aino_na=int(input("Su aino de nacimiento es: "))
num_hijos=int(input("Su numero de hijos es: "))
aino_banc=int(input("Su año de pertenencia al banco es: "))
est_civil=input("Su estado civil es Soltero(1) o Casado(2): ")
viv=input("Usted vive en Urbano(3) o Rural(4): ")

S=1
C=2
U=3
R=4

if (aino_banc>10) and (num_hijos>=2):
        print("APROBADO")
        if (aino_banc<=10) and (num_hijos<2):
            print("RECHAZADO")
if (est_civil==2) and (num_hijos>3) and (aino_na>=1967 or aino_na>=1977):
    print("APROBADO")
    if (est_civil!=2) and (num_hijos<3) and (aino_na<1967 or aino_na>1977):
        print("RECHAZADO")
if (ing>2500000) and (est_civil==1) and (viv==4):
    print("APROBADO")
    if (ing<=2500000) and (est_civil!=1) and (viv!=3):
        print("RECHAZADO")
if (ing>3500000) and (aino_banc>5):
    print("APROBADO")
    if (ing<=3500000) and (aino_banc<=5):
        print("RECHAZADO")
if (viv==4) and (est_civil==2) and (num_hijos<2):
    print("APROBADO")
    if (viv!=4) and (est_civil!=2) and (num_hijos>=2):
        print("RECHAZADO")
