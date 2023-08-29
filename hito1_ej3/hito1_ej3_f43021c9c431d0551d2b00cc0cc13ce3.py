print("Por favor responda las siguientes preguntas para la aprobación del crédito")
ingreso=int(input("Ingrese su ingreso mensual: "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese el número de hijos: "))
pertenencia=int(input("Ingrese el número de años de pertenencia al banco: "))
estado=("Ingrese su estado civil (C si esta casado o S si esta soltero): ")
vive=("Ingrese si R si vive en el campo o U si vive en la zona urbana: ")
if 2016-pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado== "C" and hijos>3 and 45< 2016-nacimiento<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="C":
    print("APROBADO")
elif ingreso>3500000 and pertenencia> 5:
    print("APROBADO")
elif vive== "R" and estado== "C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")


