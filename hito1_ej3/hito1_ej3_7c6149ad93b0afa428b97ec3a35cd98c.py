#Aprobación de créditos
ing=int(input("Ingreso:"))
nac=int(input("Año nacimiento:"))
hijo=int(input("Número de hijos:"))
años=int(input("Años de pertenencia al banco:"))
est_civ=(input("Ingrese su estado civil (S:soltero,C:casado):"))
vive=(input("Ingrese U si vive en ciudad y R si vive en zona rural:"))
edad=2023-nac
if años>10 and hijo>=2:
    print("APROBADO")
elif est_civ=="C" and hijo>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ing>2500000 and est_civ=="S" and vive=="U":
    print("APROBADO")
elif ing>3500000 and años>5:
    print("APROBADO")
elif vive=="R" and est_civ=="C" and hijo<2:
    print("APROBADO")
else:
    print("RECHAZADO")