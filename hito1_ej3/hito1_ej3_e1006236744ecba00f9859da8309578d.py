#Aprobación de créditos
print("ingresar datos")
I=int(input("Ingrese el monto de sus ingresos en pesos:"))
A=int(input("Año de nacimiento:"))
N=int(input("Numero de hijos:"))
PB=int(input("Años perteneciente al banco:"))
print("Estado civil s:soltero o c:casado :")
E=str(input("Ingrese S o C:"))
S=E
C=E
print("Donde vive U: urbano R: rural")
V=str(input("Ingrese U o R"))
U=V
R=V
a=2021-A
if (PB>10 and N>=2):
    print ("APROBADO")
elif (E==C) and N>3 and a>45 and a<55:
    print("APROBADO")
elif I>2500000 and (E==S) and (V==U):
    print("APROBADO")
elif I>3500000 and PB>5:
    print("APROBADO")
elif (V==R) and (E==C) and N<2:
    print("APROBADO")
else:
    print("RECHAZADO")      