p = int(input("Ingresos en pesos:"))
n = int(input("Año de Nacimiento:"))
h = int(input("Numero de Hijos:"))
b = int(input("Años de pertenencia al banco:"))
c = str(input("Estado Civil \"S\":Soltero o \"C\":Casado :"))
v = str(input("Donde vive \"U\":Urbano o \"R\":Rural :"))
n = 2020-n
if b > 10 and h >= 2:
    print("APROBRADO")
elif c == "C" and h > 3 and 45 <= n <= 55:
    print("APROBADO")
elif p > 2500000 and c == "S" and v == "U":
    print("APROBADO")
elif p > 3500000 and b > 5:
    print("APROBADO")
elif v == "R" and c == "C" and 0 <= h < 2:
    print("APROBADO")
else :
    print("RECHAZADO")
