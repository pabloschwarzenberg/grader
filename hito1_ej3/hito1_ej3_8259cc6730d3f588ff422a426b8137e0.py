#Aprobación de créditos
a=int(input("Ingrese su ingreso: $"))
b=int(input("Ingrese su año de naciemiento: "))
h=int(input("Ingrese número de hijos: "))
d=int(input("Ingrese años de pertenencia al banco: "))
e=input("Ingrese Estado Civil: ")
f=input("Ingrese zona a la que pertenece: ")
g=2017-b
if d>10 and h>=2:
    print("APROBADO")
elif e=="C" and h>3 and 45<=n<=55:
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")