#Aprobación de créditos
I=int(input("ingrese su cantidad de ingresos:"))
A=int(input("ingrese su año de nacimiento:"))
H=int(input("ingrese cantidad de hijos:"))
P=int(input("ingrese la cantidad de años que usted pertenece al banco:"))
E=input("ingrese su estado civil si es casado ingrese C, si es soltero ingrese S:")
U=input("ingrese lugar donde vive, si es campo ingrese R, si es ciudad ingrese T:")
B=(2018-A)

if P>10 and H>=2:
    print("APROBADO")
    
elif E=="C" and H>3 and 45<=B<=55:
    print("APROBADO")

elif I>2500000 and E=="S" and U=="T":
    print("APROBADO")

elif I>3500000 and P>5:
    print("APROBADO")

elif U=="R" and E=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")
     