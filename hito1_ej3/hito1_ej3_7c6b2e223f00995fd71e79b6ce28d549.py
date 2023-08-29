#Aprobación de créditos
I=int(input("Ingreso en pesos:"))
AN=int(input("Año de Nacimiento:"))
N=int(input("Número de Hijos:"))
AP=int(input("Años de Pertenencia al Banco:"))
E=input("Estado Civil:")
V=input("Seleccione viviendo en sector Rural o Urbano")
if AP>10 and N>=2:
    print("APROBADO")
elif E=="C" and N>3:
    if AN>=1961 and AN<=1971:
        print("APROBADO")
elif I>2500000 and E=="S" and V=="U":
    print("APROBADO")
elif AP>5 and I>3500000:
    print("APROBADO")
elif V=="R" and E=="C" and N<2:
    print("APROBADO")
else:
    print("RECHAZADO")