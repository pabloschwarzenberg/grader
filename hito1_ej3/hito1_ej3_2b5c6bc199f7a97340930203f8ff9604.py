#Aprobación de créditos
a = int(input("Introduzca año de nacimiento: "))
b = int(input("Introduzca numero de hijos: "))
c = int(input("introduzca ingresos: "))
d = int(input("Introduzca año de pertenecia al banco: "))
e = str(input("Casado y soltero: "))
f = str(input("Ingrese donde vive: "))
edad = 2021 - a
if d > 10 and b >= 2:
    print("APROBADO")
elif d <= 10 and b < 2:
    print("RECHAZADO")
if e == "casado" and b > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif e!= "casado" and b < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if c > 2500000 and e == "soltero" and f == "urbano":
    print("APROBADO")
elif c < 2500000 and e != "soltero" and f != "urbano":
    print("RECHAZADO")
if c > 3500000 and d > 5:
    print("APROBADO")
elif c < 3500000 and d < 5:
    print("RECHAZADO…")      