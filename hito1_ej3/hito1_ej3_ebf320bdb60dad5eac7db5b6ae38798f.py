#Aprobación de créditos
C=casado
S=soltero
I=input("ingrese sus ingresos")
N=input("ingrese su edad")
NH=input("ingrese su numero de hijos")
F=input("Años Perteneciendo al banco")
E=input("Estado civil: soltero o casado, con una S o C mayuscula")
Z=input("Vive en zona rural o ciudad")
F=int(F)
NH=int(NH)
N=int(N)
if(F>=10 and NH>=2):
    print("aceptado")
if(E==C and NH>3 and N>44 and N<55):
    print("aceptado")

