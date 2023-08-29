#Aprobación de créditos
ingresos=int(input("Ingreso:"))
ano=int(input("Año de nacimiento:"))
hijos=int(input("Numero de hijos:"))
anos_banco=int(input("Años de pertenencia al banco:"))
estado=input("Estado civil (S:Soltero, C:Casado)")
vive=input("Vive en(U:Urbano, R:Rural):")
edad=2017-ano
if anos_banco>10 and hijos>=2 :
    print("APROBADO")
elif estado=='C' and hijos>3 and 45<=edad<=55:
    print("APROBADO")
elif ingresos>2500000 and estado=='S' and vive=='U':
    print("APROBADO")
elif ingresos>3500000 and anos_banco>5:
    print("APROBADO")
elif vive=='R' and estado=='C' and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")