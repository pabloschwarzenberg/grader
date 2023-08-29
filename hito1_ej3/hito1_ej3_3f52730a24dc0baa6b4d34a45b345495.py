I=int(input("Ingreso: "))
A=int(input("Año nacimiento: "))
H=int(input("nro hijos: "))
An=int(input("Años pertenenecia al banco"))
E=input("estado civil: S o C: ")
L=input("campo o ciudad: U o R: ")
if An>10 and H>=2:
    print("APROBADO")
elif E=="C" and H>3 and 45<=(2016-A)<=55:
    print("APROBADO")
elif I>2500000 and E=="S" and L=="U":
    print("APROBADO")
elif L=="R" and E=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      