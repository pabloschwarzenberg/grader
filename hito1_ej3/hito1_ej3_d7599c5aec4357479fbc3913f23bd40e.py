#Aprobación de créditos
I = eval(input("Ingrese su ingreso: "))
A = int(input("Ingrese su año de nacimiento: "))
N = int(input("Ingrese su número de hijos"))
P = int(input("Ingrese sus años de pertenencia al banco :"))
E = input("Indique su estado civil,S para soltero, C para casado: ")
X = input("Indique si pertenece a una población Urbana, U o Rural, R: ")

if P > 10 and N >=2:
    print("APROBADO")
elif E == "C" and N > 3 and 45 <= (2021 - A) <= 55:
    print("APROBADO")
elif I > 2500000 and E == "S" and X == "U":
    print("APROBADO")
elif I > 3500000 and P > 5:
    print("APROBADO")
elif X == "R" and E == "C" and N < 2:
    print("APROBADO")
else:
    print("RECHAZADO")