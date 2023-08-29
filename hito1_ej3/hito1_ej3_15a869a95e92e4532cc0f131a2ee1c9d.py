#Aprobación de créditos
i = int(input("Ingreso:"))
a = int(input("Año de nacimiento:"))
n = int(input("Numero de hijos:"))
p = int(input("Años de presencia en el banco:"))
e = str(input("Estado civil:"))
d = str(input("Donde vive:"))

edad = 2021 - a

if p>=10:
    print("APROBADO")
elif n>=2:
    print("APROBADO")
elif e==("CASADO"):
    print("APROBADO")
elif edad==45:
    print ("APROBADO")
elif edad==55:
    print("APROBADO")
elif i>2500000:
    print("APROBADO")
elif i>3500000:
    print("APROBADO")
elif p>5:
    print("APROBADO")
elif d==("CAMPO"):
    print("APROBADO")
elif n<2:
    print("APROBADO")
elif e==("SOLTERO"):
    print("APROBADO")
elif d==("CIUDAD"):
    print("APROBADO")   