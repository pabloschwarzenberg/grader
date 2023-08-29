#Aprobación de créditos
a=float(input("ingrese su ingreso en pesos:"))
b=float(input("ingrese su año de nacimiento:"))
h=float(input("ingrese su numero de hijos:"))
d=float(input("ingrese sus años de pertenencia al banco:"))
e=input("ingrese su estado civil, soltero= S , casado= C :")
f=input("si es de:campo= R, ciudad= U:")

edad= 2020-b

if d>10 and h>=2:
    print("APROBADO")
elif e=="C" and h>3 and  45<=edad<=55:
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      