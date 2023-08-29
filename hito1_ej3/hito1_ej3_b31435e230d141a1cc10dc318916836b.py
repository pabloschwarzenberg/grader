#Aprobación de créditos
i = int(input("Ingresos(en pesos): "))
a = int(input("Año de nacimiento: "))
h = int(input("Numero de hijos: "))
pb = int(input("Años de pertenencia al banco: "))
e = str(input("Estado civil: "))
c = str(input("Donde vive: "))

edad = 2021 - a

if pb >= 10:
    print("APROBADO")
elif h >= 2:
    print("APROBADO")
elif e == ("casado"):
    print("APROBADO")
elif edad == 45:
    print("APROBADO")
elif edad == 55:
    print("APROBADO")
elif i > 2500000:
    print("APROBADO")
elif i > 3500000:
    print("APROBADO")
elif pb > 5:
    print("APROBADO")
elif c == ("campo"):
    print("APROBADO")
elif h < 2:
    print("APROBADO")
elif e == ("soltero"):
    print("APROBADO")
elif c == ("ciudad"):
    print("APROBADO")
