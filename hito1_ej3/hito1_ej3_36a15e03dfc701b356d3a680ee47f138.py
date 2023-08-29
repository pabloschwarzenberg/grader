#VARIABLES#
ingr=0
year=0
hijos=0
perma=0
ec=0
ur=0
#INPUT#
print("Para poder postular a nuestro credito de consumo necesitaremos que completes tus datos a continuacion")
ingr=int(input("Digite su ingreso mensual: "))
year=int(input("Ingrese su edad: "))
hijos=int(input("Cuantos hijos tiene?: "))
perma=int(input("Cuantos años a permanecido a nuestro banco?: "))
ec=str(input("Cual es su estado civil?(Si es solero S o C si es casado): "))
live=(str(input("Actualmente reside en campo o ciudad? U: urbano, R: rural: ")))
#PROGRAMA#
if perma >=10 and hijos >=2:
    print("APROBADO")
elif ec=="C" and hijos>=3 and year >=45 and year<55:
    print("APROBADO")
elif ingr >=2500000 and ec=="S" and live=="U":
    print("APROBADO")
elif ingr >=3500000 and perma >=5:
    print("APROBADO")
elif live=="R" and hijos <2:
    print("APROBADO")
else:
    print("RECHAZADO")