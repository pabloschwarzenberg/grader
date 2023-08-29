i=int(input("Ingrese sus ingresos: "))
n=int(input("Ingrese año de nacimiento: "))
h=int(input("Ingrese numero de hijos: "))
a=int(input("Ingrese años de pertenencia al banco: "))
e=input("Ingrese su estado civil; s=soltero, c=casado: ")
y=input("Ingrese si vive en campo o ciudad; u=urbano, r=rural: ")


if a>10 and h>=2:
    print("APROBADO")
    
elif e=="c" and h>3 and 1962<=n<=1972:
    print("APROBADO")

elif i>2500000 and e=="s" and y=="u":
    print("APROBADO")
    
elif i>3500000 and a>5:
    print("APROBADO")
    
elif y=="R" and e=="C" and h<2:
    print("APROBADO")

else:
    print("RECHAZADO")