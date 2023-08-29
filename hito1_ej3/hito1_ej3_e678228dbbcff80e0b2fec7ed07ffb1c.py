#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
añonac=int(input("Año de nacimiento "))
hijos=int(input("Número de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
estciv=input("Estado civil soltero o casado (S/C) ")
vivienda=input("Si vive en un ambiente urbano o rural (R/U): ")


edad=2021-añonac

if(banco>10 and hijos>=2):
    print("APROBADO")

if(estciv=="C" and hijos>3 and edad>=45 and edad<=55):
    print("APROBADO")

if(ingreso>2500000 and estciv=="S"  and  vivienda=="U"):
    print("APROBADO")

if(ingreso>3500000 and banco>5):
    print("APROBADO")

if(vivienda=="R" and  estciv=="C" and hijos<2):
    print("APROBADO")

else:
    print("rechazado")