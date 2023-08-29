#Aprobación de créditos
ingreso=int(input("Indica tus ingresos: "))
edad=int(input("Indica edad: "))
hijos=int(input("Indica cantidad de hijos: "))
pertenencia=int(input("Ingresa años de pertenencia la banco: "))
estado=str(input("Indica si eres casado (C) o eres soltero(S)"))
vive=str(input("Indica si vives en el campo(R) o vives en la ciudad(U): "))

if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and edad>=44 and edad <=55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      