#Aprobación de créditos
i=int(input("ingreso:"))
an=int(input("año de nacimiento:"))
n=int(input("numero de hijos:"))
ap=int(input("años de pertenecia al banco:"))
ec=(input("estado civil:"))
v=(input("Urbano o Rural:"))
edad=2016-an
if(((ap>10)and(n>=2))or((ec=="C")and(n>3)and(45<=edad<=55))or((i>2500000)and(ec=="S")and(v=="U"))or((i>3500000)and(ap>5))or((v=="R")and(ec=="C")and(n<2))):
    print("APROBADO")
else:
    print("RECHAZADO")
    