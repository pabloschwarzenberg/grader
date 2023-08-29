#Aprobación de créditos
i = int(input("Ingreso: "))
y = int(input("Año de Nacimiento: "))
c = int(input("Numero de Hijos: "))
a = int(input("Años de pertenencia: "))
e_c = str(input("Estado civil: "))
v = str(input("Sector donde vive: "))
y = 2020 - y
if v == 'U' and e_c == 'S' and i >= 2500000:
    print("APROBADO")
elif v == 'R' and e_c == 'C' and c < 2:
    print("APROBADO")
elif a > 5 and i >= 3500000:
    print("APROBADO")
elif a > 10 and c >= 2:
    print("APROBADO")
elif c > 3 and e_c == 'C' and 45 <= y <= 55:
    print("APROBADO")
else:
    print("RECHAZADO")