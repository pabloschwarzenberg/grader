i=int(input("Ingreso (en pesos): "))
a=int(input("Año de nacimiento: "))
h=int(input("Número de hijos: "))
A=int(input("Años de pertenencia al banco: "))
e=input("Estado civil (S: soltero, C, casado): ")
s=input("Si vive en campo o cuidad (U: urbano, R: rural): ")
u=2020-a
if A>10 and h>=2:
    print("APROBADO")
elif e in "cC" and h>=3 and 45<=u<=55:
    print("APROBADO")
elif i>2500000 and e in "sS" and s in "uU":
    print("APROBADO")
elif i>3500000 and A>5:
    print("APROBADO")
elif s in "rR" and e in "cC" and h <2:
    print("APROBADO")
else:
    print("No aprobado")