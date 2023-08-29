#Aprobación de créditos

d = int(input("ingresos:"))
n = int(input("año de nacimiento:"))

edad = 2021 - n

h = int(input("numero de hijos:"))
a = int(input("años de pertenencia al banco:"))
e = str(input("estado civil(S soltero C casado):"))
v = str(input("vive en ciudad o campo(U urbano, R rural):"))

#1
if a > 10 and h >= 2:

    print ("APROBADO")

#2
elif e == ("C") and h > 3 and edad in range (45,56):

    print ("APROBADO")

#3
elif d > 2500000 and e == ("S") and v == ("U"):

    print("APROBADO")

#4
elif d > 3500000 and a > 5:

    print("APROBADO")

#5
elif v == ("R") and e == ("C") and h < 2:

    print("APROBADO")

elif a:

    print("RECHAZADO")
