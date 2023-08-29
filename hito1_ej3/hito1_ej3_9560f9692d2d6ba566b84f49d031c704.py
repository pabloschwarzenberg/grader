a=int(input("ingresar cantidad de ingresos: "))
b=int(input("ingresar año de nacimiento: "))
c=int(input("ingresar n de hijos: "))
d=int(input("ingresar años de permanencia: "))
e=(input("ingresar estadi civil: "))
f=(input("ingresar donde vive: "))


if a>10 and c>=2:
    print("APROBADO")


elif e=="C" and c>3 and b>1976 and b<1966:
    print("APROBADO")


elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")


elif a>3500000 and d>5:
    print("APROBADO")


elif f=="R"  and e=="C" and c<2:
    print("APROBADO")


else:
    print("RECHAZADO")




