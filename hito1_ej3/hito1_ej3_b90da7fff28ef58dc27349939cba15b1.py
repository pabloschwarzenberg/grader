i=eval(input("Su ingreso: "))
a=eval(input("Año de nacimiento: "))
h=eval(input("Cantidad de hijos: "))
p=eval(input("Años de pertenencia al banco: "))
e=input("Estado civil, Soltero es S y Casado es C: ")
v=input("Donde vive, Campo es R y Ciudad es U: ")

A=2020-a

if p>=10 and h>=2:
   print("APROBADO")
elif e==str("C") and h>3 and (A>=45 and A<=55):
    print("APROBADO")
elif i>2500000 and e==str("S") and v==str("U"):
    print("APROBADO")
elif i>3500000 and p>5:
    print("APROBADO")
elif v==str("R") and e==str("C") and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")