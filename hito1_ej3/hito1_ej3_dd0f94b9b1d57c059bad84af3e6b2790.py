#Aprobación de créditos
ingreso=int(input("ingreso:"))
año=int(input("año:"))
hijos=int(input("hijos:"))
pertenencia=int(input("años de pertenencia:"))
estado=input("estado civil:")
lugar=input("lugar:")
edad=(2020-año)
if pertenencia>10 and hijos>=2:
    print("APROBADO")
if estado=="C" and hijos<3 and 45<edad<55:
    print("APROBADO")
if ingreso>2500000 and estado=="S" and lugar=="U":
    print ("APROBADO")
if ingreso>3500000 and pertenencia>5:
    print("APROBADO")
if lugar=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
    