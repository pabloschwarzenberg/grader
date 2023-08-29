#Aprobación de créditos
print("ingrese los siguientes datos")
ingreso = int(input("sueldo: $"))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("cantidad de hijos: "))
banco = int(input("Años de pertenencia al banco: "))
estado = input("Estado civil S(soltero) o C(casado): ")
dondeVive = input("vive en campo(R) o cuidad(U): ")
edad = 2020-nacimiento

if banco>=10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>=3 and edad>=45 and edad<=55 or estado=="c" and hijos>=3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and dondeVive=="U" or ingreso>2500000 and estado=="s" and dondeVive=="u":
    print("APROBADO")
elif ingreso>3500000 and banco>5:
    print("APROBADO")
elif dondeVive=="r" and estado=="c" or dondeVive=="R" and estado=="C":
    print("APROBADO")
else:
    print("RECHAZADO")