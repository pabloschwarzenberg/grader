#Aprobación de créditos
a=float(input("Ingrese su ingreso en pesos:"))
b=float(input("Ingrese su año de nacimiento:"))
h=float(input("Ingrese su número de hijos:"))
d=float(input("Ingrese sus años de pertenencia al banco:"))
e=input("Ingrese su estado civil, soltero= S , casado= C:")
f=input("Ingrese si es de campo o ciudad: campo= R , ciudad= U:")

edad= 2020-b

if d>10 and h>=2:
    print("APROBADO")
elif e=="C" and h>3 and 45<=edad<=55:
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")
    