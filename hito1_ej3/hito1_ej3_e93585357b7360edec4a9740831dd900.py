I=int(input("ingrese su pesos: "))
a=int(input("ingrese su año de nacimiento: "))
h=int(input("ingrese cuantos hijos tiene: "))
a2=int(input("ingrese años banco: "))
ec=input("ingrese si es soltero S o casado C: ")
v=input("ingrese donde vive, urbano U o rural R: ")

if a2>10 and h>=2:
    print("APROBADO")
elif ec == "C" and h>3 and a>=45 and a<=55:
    print("APROBADO")
elif I>2500000 and ec == "S" and v == "U":
    print("APROBADO")
elif I>3500000 and a2>5:
    print("APROBADO")
elif v == "R" and ec == "C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")  
    