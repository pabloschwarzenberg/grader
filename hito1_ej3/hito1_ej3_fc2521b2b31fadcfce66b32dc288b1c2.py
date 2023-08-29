#Aprobación de créditos
ingreso=input("ingreso:")
nacimiento=input("año de nacimiento:")
hijos=input("numero de hijos:")
años_en_banco=input("años en el banco:")
estado=input("estado civil:")
zona=input("zona donde vive:")
ingreso=int(ingreso)
hijos=int(hijos)
nacimiento=int(nacimiento)
años_en_banco=int(años_en_banco)
años=2017-nacimiento
años=int(años)
if años_en_banco>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 45<años<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and zona=="U":
    print("APROBADO")
elif ingreso>3500000 and años_en_banco>5:
    print("APROBADO")
elif zona=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("REPROBADO")    