s=1
c=0
r=2
u=3
I=int(input("Ingresos: "))
AN=int(input("año de nacimiento: "))
NH=int(input("Nº de hijos: "))
AP=int(input("Años de pertenencia al banco: "))
EC=input("Ingrese su estado civil(S: soltero, C: casado): ")
CC=input("Indique si vive en campo(R) o ciudad(U): ")
if AP>10 and NH>2:
    print("Aprobado")
elif EC==c and NH>3 and 2018-AN>45 and 2018<55:
    print("Aprobado")
else I>2500000 and EC==1 and CC==3:
    print("Aprobado")
else I>3500000 and AP>5