ingreso=int(input("ingreso en pesos"))
nacimiento=int(input("añ nacimiento"))
hijos=int(input("cantidad hijos"))
añopertenencia=int(input("año pertenencia"))
estado=input("S o C")
vive=input("U o R")
if añopertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 55>(2016-nacimiento)>45:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")