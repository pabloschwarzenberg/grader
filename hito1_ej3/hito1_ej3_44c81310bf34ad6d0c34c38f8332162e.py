#Aprobación de créditos
x=float(input("ingreso(pesos):"))
y=int(input("año de nacimiento:"))
z=int(input("numero de hijos:"))
x2=int(input("años de pertenencia al banco:"))
x3=input("estado civil:s:soltero,c:casado:")
x4=input("si vive en campo o ciudad(U:urbano,R:rural:")
años=(2020-y)


if (x2 > 10)and(z >= 2 ):
    print("APROBADO")
else:
    if ("C" == x3)and((años >= 45)or(años <= 55)):
        print("APROBADO")
    if (x > 2500000)and(x3 == S)and(x4 == U):
        print("APROBADO")
    if (x > 3500000)and(x2 > 5):
        print("APROBADO")
    if (x4 == "R")and(x3 == "C")and(z < 2):
        print("APROBADO")

    print("RECHAZADO")
