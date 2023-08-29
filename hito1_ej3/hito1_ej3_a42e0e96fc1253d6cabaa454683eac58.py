#Aprobación de créditos
ingreso=int(input("ingreso: "))
nacimiento=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
anosbanco=int(input("años de pertencia al banco: "))
estado=str(input("estado civil(S:soltero,C:casado):"))
vive=str(input("donde vive(U:urbano,R:rural):"))

if anosbanco > 10 and hijos >= 2:
    print("APROBADO")
elif estado=="C" and hijos > 3 and 1971 > ingreso > 1961:
    print("APROBADO")
elif ingreso > 2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso > 3500000 and anosbanco > 5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

      