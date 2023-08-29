#Aprobación de créditos
I=int(input("Ingreso (en pesos): "))
A=int(input("Año de nacimiento: "))
H=int(input("Número de hijos: "))
P=int(input("Años de pertenencia al banco: "))
E=input("Estado civil: ")
U=input("Paisaje urbano: ")
P1=0
H1=0
I1=0
A1=0


if P>10 and H>=2:
    print("APROBADO")
elif E=="C"  and H>3 and A=="1970" or A=="1971" or A=="1972"or A=="1973" or A=="1974" or A=="1975" or A=="1976" or A=="1977" or A=="1978" or A=="1979" or A=="1980" or A=="1981" or A=="1982" or A=="1983":
    print("APROBADO")
elif I+I1>2500000 and E=="S" and U=="U":
    print("APROBADO")
elif I+I1>3500000 and P>5:
    print("APROBADO")
elif  U=="R" and E=="C"  and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")