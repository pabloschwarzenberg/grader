#Aprobación de créditos
i=int(input("Ingrese ingreso en pesos: "))
a=int(input("Ingrese su año de nacimiento: "))
n=int(input("Ingrese numero de hijos/as: "))
t=int(input("Ingrese años de pertenencia al banco: "))
e=str(input("Ingrese su estado civil (S= soltero/a, C= casado/a):"))
C=e
S=e
l=str(input("Ingrrse si vive en campo o ciudad (R= rural, U= urbano): "))
U=l
R=l

if t>10 and n>= 2:
 print("APROBADO")
elif e==C and n>=3 and 1963<=n<=1973:
 print("APROBADO")
elif i>2500000 and e==S and l==U:
 print("APROBADO")
elif i>3500000 and t>5:
 print("APROBADO")
elif l==R and e==C and n<=2:
 print("APROBADO")
else:
 print("RECHAZADO")