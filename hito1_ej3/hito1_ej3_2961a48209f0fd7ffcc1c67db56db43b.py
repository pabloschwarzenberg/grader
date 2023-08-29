#Aprobación de créditos
ingresos= int(input("Ingrese sus ingresos en pesos:"))
año= int(input("Ingrese su año de nacimiento:"))
hijos= int(input("Ingrese su numero de hijos:"))
añosbanco= int(input("Ingrese la cantidad de años que esta en el banco:"))
civil= input("Ingrese su estado civil:(S) soltero o (C) casado:")
lugar= input("Ingrese su lugar de vivienda: (U) urbano o (R)rural:")
edad= 2020-año
if (añosbanco>10 and hijos>2):
    print("APROBADO")
elif(civil=="C" and hijos>3 and edad>=45 and edad<=55):
    print("APROBADO")
elif(ingresos>250000 and civil=="S" and lugar=="U"):
    print("APROBADO")
elif(ingresos>3500000 and añosbanco>5):
    print("APROBADO")
elif(lugar== "R" and civil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")