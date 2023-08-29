#Aprobación de créditos
ingreso=int(input())
año=int(input())
hijos=int(input())
años_de_pertenencia_al_banco=int(input())
estado_civil=input("Si es soltero ponga S si es casado ponga C")
donde_vive=input("Si vive en urbano ponga U si es rural ponga R")
if años_de_pertenencia_al_banco>10 and hijos>=2:
    print("APROBADO")
elif estado_civil=="C" and hijos>=3 and 45<año<55:
    print("APROBADO")
elif ingreso>2500000 and estado_civil=="S" and donde_vive=="U":
    print("APROBADO")
elif ingreso>3500000 and años_de_pertenencia_al_banco>5:
    print("APROBADO")
elif donde_vive=="R" and estado_civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
