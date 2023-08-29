ingreso=int(input())
año=int(input())
hijos=int(input())
pertenencia=int(input())
estado=str(input())
domicilio=str(input())
if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 45<años<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and domicilio=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia>5:
    print("APROBADO")
elif domicilio=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
