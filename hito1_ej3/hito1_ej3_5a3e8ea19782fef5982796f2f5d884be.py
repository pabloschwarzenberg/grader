#Aprobación de créditos
ingreso=int(input("Ingreso :"))
nacimiento=int(input("Ingrese año de nacimiento"))
hijos=int(input("Número de hijos "))
pertenencia=int(input("Ingrese años de pertenencia al banco "))
estado=input("Estado civil ")
vive=input("donde vive ")
edad=2020-nacimiento
if 10 < pertenencia and 2 <= hijos :
    print("APROBADO")
else :
    print("RECHAZADO")
if estado=="C" and 3 < hijos and 45<=edad<=55:
    print("APROBADO")
else :
    print("RECHAZADO")
if ingreso>2500000 and estado=="S" and vive=="U":
    print('APROBADO')
if ingreso>3500000 and pertenencia>5:
    print('APROBADO')
if vive=="R" and estado=="C" and hijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')  