ingreso=int(input("Ingrese ingreso individuo: "))
nacimiento=int(input("Ingrese año de nacimiento: "))
hijos=int(input("Ingrese numero de hijos: "))
pertenencia=int(input("Ingrese años de pertenencia en el banco: "))
estado=str(input("Ingrese estado civil S si es soltero, C si es casado: "))
S=str(estado)
C=str(estado)
vive=str(input("Ingrese si vive en U urbano o R rural: "))
U=str(vive)
R=str(vive)

anos=2022-nacimiento
if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado==C and hijos>3 and (anos>=45 and anos<=55):
    print("APROBADO")
elif ingreso>=2500000 and estado==S and pertenencia>=5:
    print("APROBADO")
elif ingreso>=3500000 and pertenencia>5:
    print("APROBADO")
elif vive==R and estado==C and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
