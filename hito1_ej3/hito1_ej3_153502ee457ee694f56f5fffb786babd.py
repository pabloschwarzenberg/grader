#Aprobación de créditos
pesos=int(input("ingrese sus ingresos:"))
año=int(input("ingrese su año de nacimiento:"))
hijos=int(input("ingrese cuantos hijos tiene:"))
banco=int(input("ingrese pertenencia al banco:"))
estado=input("ingrese su estado civil:")
vive=input("ingrese donde vive:")
edad=2023-año

if banco>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 45<=edad<=55:
    print("APROBADO")
elif pesos>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif pesos>3500000 and banco>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")      