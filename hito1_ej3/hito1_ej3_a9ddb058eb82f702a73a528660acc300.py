#Aprobación de créditos
ingreso=int(input("escriba sus ingresos:"))
nacimiento=int(input("ingrese su año de nacimiento:"))
hijos=int(input("ingrese numero de hijos:"))
per=int(input("ingrese la cantidad de años de pertenencia al banco:"))
estado=input("ingrese su estado civil, S(soltero) o C(casado):")
residencia=input("ingrese su lugar de recidencia, U(urbano/ciudad) o R(rural/campo):")
if per>= 10 and hijos>= 2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 1967<=nacimiento<=1977:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and residencia=="U":
    print("APROBADO")
elif ingreso>3500000 and pert>5:
    print("APROBADO")
elif residencia=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO ")