#Aprobación de créditos
a=int(input("Ingreso (en pesos):"))
b=int(input("Año de nacimiento:"))
c=int(input("Numero de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=str(input("Estado civil soltero " "S" " y ""casado ""C :"))
f=str(input("Urbano ""U"" o Rural ""R :"))

edad = (2020 - b)

if d > 10 and c >= 2:
    print("APROBADO")
elif e == "C" and c > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif a > 2500000 and e == "S" and f == "U":
    print("APROBADO")
elif a > 3500000 and d > 5:
    print("APROBADO")
elif f == "R" and e == "C" and c < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    