i=int(input("Ingrese sus ingresos en valor de pesos: "))
n=int(input("Ingrese su año de nacimiento: "))
h=int(input("Ingrese número de hijos: "))
p=int(input("Ingrese los años que tiene de pertenencia al banco: "))
e=input("Ingrese su estado civil. Ingrese una 's' si su estado es soltero/a, o ingrese 'c' si su estado es casado/a: ")
v=input("Ingrese 'u' o 'r' (urbano y rural respectivamente) para indicar si vive en campo o ciudad: ")
c=e
C=e
s=e
S=e
u=v
U=v
l=v
L=v
F= (2020 - n)

if (p>10) and (h>=1):
    print("APROBADO")
elif ((e==c) or (e==C)) and (h>3) and (45<=F<=55):
    print("APROBADO")
elif (i>2500000) and ((e==s) or (e==S)) and ((v==u) or (v==U)):
    print("APROBADO")
elif ((i>3500000) and (p>5)):
    print("APROBADO")
elif ((v==l or v==L) and (e==c or e==C) and (i<2)):
    print("APROBADO")
else:
    print("RECHAZADO")
    