#Aprobación de créditos
i = float(input("Ingresos ($): "))
a = int(input("Año de nacimiento: "))
h = int(input("Numero de hijos: "))
b = int(input("Años de pertenencia al banco: "))
e = str(input("Estado Civil (S o C): "))
v = str(input("Vive en Campo (R) o Ciudad (U): "))

edad = 2021-a


if b>10 and h>=2:
    print("APROBADO")

elif e=="c" and h>3 and 45<=edad<=55 :
    print("APROBADO")

elif i>2500000 and e=="S" and v==U:
    print("APROBADO")

elif i>3500000 and b>5:
    print("APROBADO")

elif v=="R" and e=="C" and h<2:
    print("APROBADO")

else:
    print("RECHAZADO")