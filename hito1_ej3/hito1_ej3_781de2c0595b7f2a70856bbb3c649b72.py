#Aprobación de créditos
x1=float(input("ingrese su ingreso en pesos porfavor:"))
x2=float(input("ingrese su año de nacimiento porfavor:"))
x3=float(input("ingrese su numero de hijos porfavor:"))
d=float(input("ingrese sus años de pertenencia al banco porfavor:"))
e=input("ingrese su estado civil, soltero= S , casado= C porfavor:")
f=input("si es de:campo= R, ciudad= U porfavor:")

edad= 2020-x2

if d>10 and x3>=2:
    print("APROBADO")
elif e=="C" and x3>3 and  45<=edad<=55:
    print("APROBADO")
elif x1>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif x1>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and x3<2:
    print("APROBADO")
else:
    print("RECHAZADO")