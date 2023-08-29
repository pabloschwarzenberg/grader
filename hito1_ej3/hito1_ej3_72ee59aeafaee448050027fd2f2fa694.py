print("ingrese los siguientes datos ")
a=int(input("ingreso pesos: "))
b=int(input("año de nacimiento: "))
c=int(input("numero de hijos:"))
d=int(input("años de pertenencia al banco: "))
e=input("estado civil (S si es soltero o C si es casado): ")
f=input("lugar donde vive (U si es urbano o R si es rural): ")

S=e
C=e
U=f
R=f



if (d>10 and c>=2) or (e==C and c>3 and 1973<b<1963) or (a>2500000 and e==S and f==U) or (a>3500000 and d>5) or (f==R and e==C and c<2):
  print ("APROBADO")
else:
  print("RECHAZADO")
  