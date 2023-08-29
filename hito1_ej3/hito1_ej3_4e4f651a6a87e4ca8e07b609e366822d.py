#Aprobación de créditos
a=int(input("Ingreso :"))
b=int(input("Año de nacimiento :"))
c=int(input("Número de hijos :"))
d=int(input("Años de pertenencia al banco :"))
e=input("Estado civil (S:Soltero, C:Casado) :")
f=input("Localidad ( U:Urbano, R:Rural) :")
g=2016-b
if (d>=10) and (c>=2):
     print("APROBADO")
elif (e=="C") and (c>3) and (45<=g<=55):
    print("APROBADO")
elif (a>2500000) and (e=="S") and (f=="U"):
    print("APROBADO")
elif (a>3500000) and (d>5):
    print("APROBADO")
elif (f=="R") and (e=="C") and (c<2):
    print("APROBADO")
else :
    print("RECHAZADO")