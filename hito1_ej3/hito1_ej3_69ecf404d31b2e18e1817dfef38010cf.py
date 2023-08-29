#Aprobación de créditos
In = int(input("Ingreso del cliente: "))
An = int(input("Año de nacimiento del cliente: "))
Nh = int(input("Numero de hijos del cliente: "))
Ap = int(input("Años de pertenencia al banco: "))
Ec = str(input("Estado civil del cliente: "))
Vi = str(input("Urbano o Rural: "))
Ed = (2018- An)

if Ap>=10 and Nh>=2:
    print("APROBADO")
if Ec == "C" and Nh>3 and 45<= Ed <=55:
    print("APROBADO")
if In>2500000 and Ec == "S" and Vi == "U":
    print("APROBADO")
if In>3500000 and Ap>5:
    print("APROBADO")
if Vi== "R" and Ec== "C" and Nh<2:
    print("APROBADO")
