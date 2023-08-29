#Aprobación de créditos
i=int(input("Ingrese su ingreso en pesos: "))
a=int(input("Ingrese su año de nacimiento: "))
n=int(input("Ingrese su numero de hijos: "))
o=int(input("Ingrese su año de pertenencia al banco: "))
e=str(input("Ingres su estado civil, s= soltero/a, c=casado/a ")) 
v=str(input("Ingrese lugar donde vive, u=urbano, r:rural: "))
S=e
C=e
R=v
U=v

if o>10 and n>=2:
  print("APROBADO")
elif C==e and n>3 and 45<a<55:
  print("APROBADO")
if i>2500000 and S==E and U==v:
  print("APROBADO")
if i>3500000 and o>5:
  print("APROBBADO")
if R==v and C==e and n<2:
  print("APROBADO")

else:
  print("RECHAZADO")