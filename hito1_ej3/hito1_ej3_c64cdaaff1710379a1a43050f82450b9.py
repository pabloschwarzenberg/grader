#Aprobación de créditos
a=int(input("Dame tu ingreso"))
b=int(input("Dame tu feha de nacimiento"))
c=int(input("Cuantos hijos tienes"))
d=int(input("Hace cuantos años perteneces al banco"))
e=input("Cual es tu estado civil")
f=input("En donde vives")
g=2017
if d>10 and c>=2:
  print("APROBADO")
elif e=="C" and c>3 and 45<g-b<55:
  print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
  print("APROBADO")
elif a>3500000 and d>5:
  print("APROBADO")
elif f=="R" and e=="C" and c<2:
  print("APROBADO")
else:
  print("RECHAZADO")
 

