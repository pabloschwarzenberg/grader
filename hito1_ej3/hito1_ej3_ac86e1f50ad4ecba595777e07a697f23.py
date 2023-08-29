#Aprobación de créditos
I=int(input("Indique sus ingresos en pesos: "))
A_N=int(input("Indique su año de nacimiento: "))
N_H=int(input("Indique el numero de hijos: "))
A_P=int(input("Indique sus años de pertenencia al banco: "))
E_C=input("Indique su estado civil (S: soltero, C: casado): ")
D_V=input("Indique si vive en campo o cuidad (U: urbano, R: rural): ")
cont=0

edad=2022-A_N
if A_P>=10 and N_H>=2:
  cont=cont+1
if E_C=="C" and N_H>3 and (edad>=45 and edad<=55):
  cont=cont+1
if I>=2500000 and E_C=="S" and D_V=="U":
  cont=cont+1
if I>=3500000 and A_P>5:
  cont=cont+1
if D_V=="R" and E_C=="C" and N_H<2:
  cont=cont+1
if cont>0:
  print("APROBADO")
else:
  print("RECHAZADO")
     