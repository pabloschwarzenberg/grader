#Aprobación de créditos
ingreso=int(input("ingreso (en pesos): "))
a=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
civil=input("Estado civil (soltero (s),casado (c): ")
lugar= input("Si vive en campo o cuidad ((U)urbano, (r)rural): ")
a2=2020-a
if banco>=10 and hijos>=2 :
    print("APROBADO")
if civil=="C" and hijos>=3 and 45<=a2<=55:
    print("APROBADO")
if civil=="S" and ingreso>=2500000 and lugar == "U":
    print("APROBADO")
if ingreso>=3500000 and banco>=5:
    print("APROBADO")
if lugar=="R" and hijos<=2:
    print("APROBADO")
else:
    print("RECHAZADO")