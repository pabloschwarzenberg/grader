#Aprobación de créditos
ingreso=int(input("Ingrese sus ingresos economicos: "))
año=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
pertenencia=int(input("Ingrese sus años de pertenencia: "))
estado=input("Ingrese su estado civil (Soltero=S, Casado=C): ") #no me lo ponia correcto con la restriccion while not
casa=input("Ingrese si vive en un espacio urbano o rural (U o R): ") #no me lo ponia correcto con la restriccion while not

if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and (2020-año>=45 and 2020-año<=55):
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and casa=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia>5:
    print("APROBADO")
elif casa=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")     