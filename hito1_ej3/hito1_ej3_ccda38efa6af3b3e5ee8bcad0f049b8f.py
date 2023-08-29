#aprobación de creditos
I=int(input("Ingreso (en pesos): "))
A=int(input("Año de nacimiento "))
H=int(input("Número de hijos: "))
B=int(input("Años de pertenencia al banco: "))
E=input("Estado civil (S: soltero, C: casado): ")
V=input("Si vive en campo o cuidad (U: urbano, R: rural): ")
e=E.upper()
v=V.upper()
U=1
R=2
S=3
C=4
if(B>10 and H>=2):
    print("APROBADO")
if(e==4 and H>=3 and A in range(1966,1976)):
    print("APROBADO")
if(I>2500000 and e==3  and  v==1):
    print("APROBADO")
if(I>3500000 and B>5):
    print("APROBADO")
if(H<2 and e==4 and v==2):
    print("APROBADO")
else:
    print("APROBADO")


