#Aprobación de créditos
ingreso = int(input("ingreso (en pesos): "))
anon = int(input("año de nacimiento "))
nhijos = int(input("número de hijos: "))
anob = int(input("Años pertenencia al banco: "))
EC = str(input("Estado Civil (S: soltero, C: casado): "))
vive = str(input("viven en campo (R) o ciudad (U): "))
edad = int(2017 - anon)

if anob>10 and 2<=nhijos:
    print("APROBADO")
elif EC=="C" and nhijos>3 and 45<edad<55:
    print("APROBADO")
elif ingreso>2500000 and EC=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and anob>5:
    print("APROBADO")
elif vive=="R" and EC=="C" and nhijos<2:
    print("APROBADO")
else:
    print ("RECHAZADO")