ingreso=eval(input("ingreso:"))
ano=eval(input("ano de nacimiento:"))
hijos=eval(input("numero de hijos:"))
pertenencia=eval(input("anos de pertenencia al banco:"))
estado=input("estado civil(S:soltero, C:casado):")
vive=input("vive en(U:urbano, R:rural):")

if (pertenencia>=10 and hijos>=2):
    print("APROBADO")
elif (estado=="C" and hijos>=3 and ano>=1965 and ano<=1975):
    print("APROBADO")
elif (ingreso>=2500000 and estado=="S" and vive=="U"):
    print("APROBADO")
elif (ingreso>=3500000 and pertenencia>=5):
    print("APROBADO")
elif (vive=="R" and estado=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")