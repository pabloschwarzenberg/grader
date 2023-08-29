#Aprobación de créditos
n = int(input("Coloque sus ingresos:"))
n1 = int(input("Coloque su año de nacimiento:"))
n2 = int(input("Coloque el numero de niños:"))
n3 = int(input("Coloque sus años de pertenencia al banco:"))
n4 = str(input("Cual es su estado civil, S:Soltero y C:Casado:"))
n5 = str(input("Coloque si vive en campo o cuidad U:urbano,R: rural:"))

C = str("C")
R = str("R")
S = str("S")
U = str("U")

if n3 >= 10 and n2 >= 2:
    print("APROBADO")
elif n4 == C and n2 > 3 and (n1 >41 and n1 >55):
    print("APROBADO")
elif n > 2500000 and n4 == S and n5 == U:
    print("APROBADO")
elif n > 3500000 and n3 > 5:
    print("APROBADO")
elif n5 == R and n4 == C and n2 <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")