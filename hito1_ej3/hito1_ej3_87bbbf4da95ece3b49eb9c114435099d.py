print("Atencion al cliente banco AlverT")
print("Sistema de regulacion sobre la aprobacion de un credito")

a = int(input("Ingrese la cantidad de sus ingresos(CLP):"))
while a <= 0:
    a = int(input("Ingrese la cantidad de sus ingresos(CLP):"))
b = int(input("Ingrese año de nacimiento:"))
while b < 1900 or b > 2021:
    b = int(input("Ingrese año de nacimiento:"))
c = int(input("Ingrese su cantidad de hijos:"))
while c < 0:
    c = int(input("Ingrese su cantidad de hijos:"))
d = int(input("Ingrese sus años de antiguedad en el banco:"))
while d < 0:
    d = int(input("Ingrese sus años de antiguedad en el banco:"))
print("Ingrese su estado civil (soltero o casado)")
e = str(input("[S] o [C]:"))
while e != "S" and e != "C":
    e = str(input("[S] o [C]:"))
print("Ingrese localidad de su vivienda (urbano o rural)")
f = str(input("[U] o [R]:"))
while f != "U" and f != "R":
    f = str(input("[U] o [R]:"))
if d > 10 and c >=2:
    print("CREDITO APROBADO")
elif e == "C" and c > 3 and (2021 - b >= 45) and (2021 - b <=55):
    print("CREDITO APROBADO")
elif a > 2500000 and e == "S" and f == "U":
    print("CREDITO APROBADO")
elif a > 3500000 and d > 5:
    print("CREDITO APROBADO")
elif e == "C" and f == "R" and c < 2:
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
      