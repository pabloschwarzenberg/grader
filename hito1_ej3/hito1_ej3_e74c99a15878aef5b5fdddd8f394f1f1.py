i=int(input("Ingreso:"))
a=int(input("Año de nacimiento:"))
n=int(input("Número de hijos:"))
p=int(input("Años de pertenencia al banco:"))
ec=input("Estado civil:")
d=input("Zona")
if p>10 and n>=2:
  print("APROBADO")
elif ec=="C" and n>3 and a>1962 and a<1972:
  print("APROBADO")
elif i>2500000 and ec=="S" and d=="U":
  print("APROBADO")
elif i>3500000 and p>5:
  print("APROBADO")
elif d=="R" and ec=="C" and n<2:
  print("APROBADO")
else:
  print("RECHAZADO")