#Aprobación de créditos
ingre=int(input("Ingrese el valor de sus ingresos:"))
edad=int(input("Ingrese su edad:"))
hijo=int(input("Ingrese su cantidad de hijos:"))
años=int(input("Ingrese años de lleva afiliado al banco:"))
print("ESTADO CIVIL")
print("S-Soltero")
print("C-Casado")
estado=input("Ingrese su opción de Estado Civil:").lower()
print("¿DONDE VIVE?")
print("U-Urbano")
print("R-Rural")
vivi=input("Ingrese su opción de vivienda:").lower()

if (años>=10) and (hijo>=2):
    print("APROBADO")
elif estado=="c" and (hijo>=3) or (edad>=1965) and (edad<=1975):
    print ("APROBADO")
elif (ingre>=2500000) and estado=="s" and vivi=="u":
    print("APROBADO")
elif ingre>=3500000 and años>=5:
    print("APROBADO")
elif vivi=="r" and estado=="c" and hijo<=2:
    print ("APROBADO")
else:
    print("RECHAZADO")