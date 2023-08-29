#Aprobación de créditos
ingreso = int(input("cuales son sus ingresos?: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
numeroHijos = int(input("cuantos hijos tiene?: "))
pertenencia = int(input("ingrese años en el banco: "))
estadoCivil = input("estado civil;(soltero (S), casado (C)): ")
residencia = input("lugar de residencia; (urbano(U), rural(R)): ")
if pertenencia>= 10 and numeroHijos>= 2:
    print("APROBADO")
elif estadoCivil=="C" and numeroHijos> 3 and [1967,1997]<=nacimiento:
    print("APROBADO")
elif ingreso>2500000 and estadoCivil=="S" and residencia=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia> 5:
    print("Aprobado")
elif residencia=="R" and estadoCivil=="C" and numeroHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")