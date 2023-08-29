#Aprobación de créditos
i=int(input("Ingrese ingreso en pesos: "))
a=int(input("Ingrese año de nacimiento: "))
h=int(input("Ingrese numero de hijos: "))
p=int(input("Ingrese años de pertenencia al banco: "))
c=input("Ingrese estado civil S/C (Soltero/Casado): ")
v=input("Ingrese si vive en cambo o ciudad U/R (Urbano/Rural): ")
apb=False
if p>10 and h>=2:
    apb=True
if c=="C" and h>3 and 45<=a<=55:
    apb=True
if i>2500000 and h=="S" and v=="U":
    apb=True
if i>3500000 and p>5:
    apb=True
if v=="R" and c=="C" and h<2:
    apb=True
if apb==True:
    print("APROBADO")
else:
    print("RECHAZADO")