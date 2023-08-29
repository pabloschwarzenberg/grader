#Aprobación de créditos
V1=int(input("indique ingresos en pesos: "))
AN=int(input("indique año de nacimiento: "))
NH=int(input("indique numero de hijos: "))
AP=int(input("indique años de pertenencia al banco: "))
ec=input("si es casado(C) o soltero(S): ")
zv=input("vive en zona rural(R) o urbana(U): ")
C=ec
S=ec
R=zv
U=zv
casado= C
soltero=S
rural=R
urbana=U
AA=(2020-AN)
if AP>10 and NH>=2:
   print("APROBADO")
if ec==C and NH>3 and 45<=AA>=55:
   print("APROBADO")
if V1>2500000 and V1<=3500000 and ec==S and zv==U:
   print("APROBADO")
if V1>3500000 and AP>5 and AP<=10:
   print("APROBADO")
if zv==R and ec==C and NH<2:
    print("APROBADO")
else:
    print("RECHAZADO")