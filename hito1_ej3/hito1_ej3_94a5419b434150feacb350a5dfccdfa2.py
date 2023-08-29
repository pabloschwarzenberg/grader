a=int(input("Ingrese cuales son sus ingresos: "))
b=int(input("Ingrese el año de su nacimiento: "))
c=int(input("Ingrese numero de hijos: "))
d=int(input("Ingrese años de pertenencia en el banco: "))
e=input('Ingrese "S" si esta soltero o ingrese "C" si esta casado:' )
f=input("Si vive en campo o cuidad ('U': urbano, 'R': rural)")
g= 2021-b
if d>10 and c>=2:
    print("APROBADO")
elif e=="C" and c>3 and  (g>=45 and g<=55):
    print("APROBADO")

elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")

elif a>3500000 and d>5:
    print("APROBADO")

elif f=="R" and e=="C" and c<2:
    print("APROBADO")

else:
    print("RECHAZADO")