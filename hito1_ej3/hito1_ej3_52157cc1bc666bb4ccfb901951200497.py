#Aprobación de créditos
i = int(input("Ingresos (en pesos) "))
a = int(input("Año de nacimiento "))
nh = int(input("Numero de hijos "))
ab = int(input("Años de pertenencia al banco "))
e = str(input("Estado civil(C=casado S=soltero) "))
v= str(input("Vive en campo o ciudad (U=urbano R=rural) "))
if ab > 10 and nh >= 2:
    print("APROBADO")
elif e.lower() =="c" and nh > 3 and a >= 45 and a <= 55:
    print("APROBADO")
elif i >= 2500000 and e.lower()=="s" and v.lower()=="u":
    print("APROBADO")
elif i >= 3500000 and ab > 5:
    print("APROBADO")
elif v.lower()=="r" and e.lower()=="c" and nh < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
