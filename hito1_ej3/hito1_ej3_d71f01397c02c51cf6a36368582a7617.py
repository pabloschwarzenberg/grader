#Aprobación de créditos
a=int(input("Ingrese su sueldo en pesos: "))
b=int(input("Ingrese su año de nacimiento: "))
c=int(input("Ingrese su numero de hijos: "))
d=int(input("Ingrese años de pertenencia en el banco: "))
e=input("Ingrese S si es soltero, ingrese C si es casado: ")
f=input("Si vive en ciudad escriba U, ingrese R si vive en campo: ")
g=("APROBADO")
h=("RECHAZADO")
if d>10 and c>=2:
 print(g)
elif e=="C" and c>3 and  1962<=b<=1972:
 print(g)
elif a>2500.000 and e=="S" and f=="U":
 print(g) 
elif a>3500.000 and d>5:
 print(g)
elif f=="R" and e=="C" and c<2:
 print(g)
else:
 print(h)