#Aprobación de créditos
a=eval(input("Ingreso:"))
b=eval(input("Año de Nacimiento:"))
c=eval(input("Numero de hijos:"))
d=eval(input("Años de pertenencia:"))
e=input("Estado civil,S(soltero), C(casado):")
f=input("U(urbano), R (Rural):")
if d>10 and c>=2:
    print("APROBADO")
elif e=="C" and c>3 and 1965<= b <=1975 :
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and c<2:
    print("APROBADO")
else:
    print("REPROBADO")      