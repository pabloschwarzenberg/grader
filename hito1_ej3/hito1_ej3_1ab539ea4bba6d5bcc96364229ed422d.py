#Aprobación de créditos
I=float(input("Ingresos: "))
N=float(input("Nacimiento: "))
H=float(input("Numero de hijos: "))
P=float(input("Años de pertenencia: "))
E=input("Estado Civil:")
V=input("Rural o Urbano:")

if P>10 and H>=2:
    print("APROBADO")
elif E=="C" and H>3 and N>=1961 and N<=1971:
    print("APROBADO")
elif I>=2500000 and E=="S" and V=="U":
    print("APROBADO")
elif I>3500000 and P>5:
    print("APROBADO")
elif V=="R" and E=="C" and H<=2:
    print("APROBADO")
else:
    print("RECHAZADO")

      