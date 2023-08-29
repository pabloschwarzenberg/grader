#Aprobación de créditos
print("--------------Ingrese sus datos-----------")
#Entradas
#Pedir datos a usuarios 
I=int(input("Ingrese el monto de sus ingresos en pesos:"))
A=int(input("Año de nacimiento:"))
H=int(input("Numero de hijos:"))
PB=int(input("Años perteneciente al banco:"))
print("Estado civil s:soltero o c:casado :")
E=str(input("Ingrese S o C: "))
S=E
C=E
print("Donde vive U:urbano R:rural")
V=str(input("Ingrese U o R "))
U=V
R=V
a=2021-A
if (PB>10 and H>=2):
    print ("APROBADO")
elif (E==C) and H>3 and a>45 and a<55:
    print("APROBADO")
elif I>2500000 and (E==S) and (V==U):
    print("APROVADO")
elif I>3500000 and PB>5:
    print("APROBADO")
elif (V==R) and (E==C) and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")
