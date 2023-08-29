#Aprobación de créditos
#Sebastian Amigo
ingreso=int(input("Digite sus ingresos en pesos: "))
agno_nacimiento=int(input("Digite su año de nacimeinto: "))
edad=agno_nacimiento-2021
n_hijos=int(input("¿Cuantos hijos tiene?: "))
agnos_banco=int(input("¿Cuantos años lleva siendo cliente del banco?: "))
es_civil=input("¿Cual es su estado civil?(S=soltero)o(C=casado): ")
camp_ciu=input("¿En donde vive usted?(U=urbano)o(R=rural): ")
if(10<agnos_banco and 2<=n_hijos):
    print("APROBADO")
elif(es_civil.upper()== "C" and 3<n_hijos and 45<=edad<=55):
    print("APROBADO")
elif(ingreso>2500000 and es_civil.upper()== "S" and camp_ciu.upper()== "C"):
    print("APORBADO")
elif(ingreso>3500000 and agnos_banco>5):
    print("APROBADO")
elif(camp_ciu.upper()== "R" and es_civil.upper()== "C" and n_hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")