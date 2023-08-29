ingreso=int(input("proporcione su ingreso:"))
nacimiento=int(input("ingrese su año de nacimiento"))
hijos=int(input("numero de hijos"))
banco=int(input("año de pertenencia al banco:"))
ec=input("ingrese su estado civil:")
residencia=input("ingrese su residencia:")
edad=(2017-nacimiento)

if banco>=10 and hijos>=2:
    print("APROBADO")
elif ec=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and ec=="S" and residencia=="U":
    print("APROBADO")
elif ingreso>3500000 and banco>5:
    print("APROBADO")
elif residencia=="R" and ec=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
