#Aprobación de créditos
print("por favor ingrese los siguientes datos...")
a=int(input("su ingreso monetario (en pesos) es: "))
b=int(input("año de nacimiento: "))
c=int(input("Numero de hijos: "))
d=int(input("años de pertenencia en el banco: "))
e=input("Estado civil (S: soltero, C: casado): ")
f=input("¿donde vive? (U: urbano, R: rural): ")
g=2017-b
int(g)
if d>10 and c>=2:
  print("APROBADO")
if e=="C" and c>3 and 45<g<55:
  print("APROBADO")
if a>2500000 and e=="S" and f=="U":
  print("APROBADO")
if a>35000000 and d>5:
  print("APROBADO")
if f=="R" and e=="C" and c<2:
  print("APROBADO")
else:
  print("RECHAZADO")     