a=int(input("Ingreso:"))
b=int(input("Año de nacimiento:"))
c=int(input("Número de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=input("Estado civil,(S=soltero,C=casado):")
m=input("U=urbano, R=rural:")


if d>10 and 2<=c:
  print("APROBADO")
elif c>3 and 1961<b<1973 and e=="S":
  print("APROBADO")
elif 2500000<a and e=="S" and m=="U":
  print("APROBADO")
elif 3500000<a and 5<d:
  print("APROBADO")
elif 2>c and m=="R" and e=="C":
  print("APROBADO")
else:
  print("RECHAZADO") 
      