ingreso=int(input("ingresos"))
nacimiento=int(input("ano de nacimiento"))
hijos=int(input("numero de hijos"))
x=int(input("anos de pertenencia"))
estado=input("soltero o casado")
vive=input("urbano o rural")
if (x>10) and (hijos>=2):
    print("APROBADO")
elif (estado=="C") and (hijos==3) and (1962<=nacimiento<=1972):
    print("APROBADO")
elif (ingreso>2500000) and (estado=="S") and (vive=="U"):
    print("APROBADO")
elif (ingreso>3500000) and (x>5):
    print("APROBADO")
elif (vive=="R") and (estado=="C") and (hijos<2):
    print("APROBADO")
else:
    print("REPROBADO")
      