#Aprobación de créditos
i = int(input("Ingreso (en pesos): "))
a = int(input("Año de nacimiento: "))
h = int(input("Número de hijos: "))
ab = int(input("Años de pertenencia al banco: "))
ec = input("Estado civil ((S): soltero, (C), casado)")
v = input("Vive en campo o cuidad ((U): urbano, (R): rural)")

if (ab > 10 and h >= 2) or (ec == "C" and h > 3 and 45 <= a <= 55) or (i > 2500000 and ec == "S" and v == "U") or (i > 3500000 and ab > 5) or (v == "R" and ec == "C" and h < 2):
    print("APROBADO")

else:
    print("RECHAZADO")