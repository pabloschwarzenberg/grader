peso = eval(input("Ingreso\n=> $"))
fecha = eval(input("Ingrese su año de nacimiento\n=> "))
hijos = eval(input("Cuantos hijos tiene usted=\n=>"))
anos = eval(input("Cuantos años ha estado con el banco?\n=> "))
Estado_civil=str(input("Ingrese su estado civil(S:soltero , C:casado)\n=> "))
vivienda=str(input("Ingrese si vive en zona rural(R) o urbana(U)\n=> "))
x="comodin"
while Estado_civil!="C" and Estado_civil!="S":
    print("Recuerde ingresar C(casado) o S(solter@)")
    Estado_civil=str(input("Ingrese su estado civil(S:solteo,C:casado\n=> "))
while vivienda!="U" and vivienda!="R":
    print("Recuerde que debe ingresar U(urbano) o R(rural)")
    vivienda=str(input("Ingrese si vive en zona rural(R) o urbana(U)\n=> "))
while hijos<0:
    print("Ingreso una cantidad invalida\nFavor de vovler a ingresar")
    hijos=eval(input("==> "))
if anos>10 and hijos>=2:
    x=("APROBADO")
    print(x)

if Estado_civil=="C" and hijos>3 and 45<=fecha<=55:
    x=("APROBADO")
    print(x)

if peso==2500000 and Estado_civil=="S" and vivienda=="U":
    x=("APROBADO")
    print(x)
if vivienda=="R" and Estado_civil=="C" and 0<=hijos<2:
    x=("APROBADO")
    print(x)
if x!="APROBADO":
    print("RECHAZADO")