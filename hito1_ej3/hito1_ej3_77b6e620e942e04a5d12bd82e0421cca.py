#Aprobación de créditos
a=int(input("ingreso en pesos= "))
b=int(input("año de nacimiento= "))
c=int(input("numero de hijos= "))
d=int(input("años de pertenencia al banco= "))
e=input("Estado civil ('S': soltero, 'C', casado)= ")
edad=2018-b
f=input("Si vive en campo o cuidad ('U': urbano, 'R': rural)= ")
if d>10 and c>=2:
    print("APROBADO")

elif e=="C" and c>3 and 45<edad and edad<55:
    print("APROBADO")

elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")

elif a>3500000 and d>5:
    print("APROBADO")

elif f=="R" and e=="C" and c<2:
    print("APROBADO")
