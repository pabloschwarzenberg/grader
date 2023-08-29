#Aprobación de créditos
i = int(input("Ingreso: "))
a = int(input("Año de nacimiento: "))
h = int(input("Número de hijos: "))
p = int(input("Años de pertenencia al banco: "))
e = input("Estado civil: ")
v = input("Locación: ")

edad = 2016-a

if (a > 10 and h >= 2):
    print("APROBADO")

elif (e == "C" and h > 3 and 45 <= edad <= 55):
    print("APROBADO")

elif (i > 2500000 and e == "S" and v == U):
    print("APROBADO")

elif (i > 3500000 and p > 5):
    print("APROBADO")

elif (v == "R" and e == "C" and h < 2):
    print("APROBADO")

else:
    print("RECHAZADO")