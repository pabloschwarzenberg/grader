#Aprobación de créditos
a = int(input("ingresos: "))
b = int(input("año de nacimiento: "))
c = int(input("numero de hijos: "))
d = int(input("años de pertenencia al banco: "))
e = input("Estado civil: ")
f = input("Vive en campo(R)o ciudad(U): ")

if d > 10 and c >= 2:
    print("APROBADO")

elif ("e == C") and c > 3:
    X = int(b)
    Y = X - 2021
    if Y > 44 and Y < 56:
        print("APROBADO")

elif a > 2500000 and ("e == S") and ("f == U"):
    print("APROBADO")

elif a > 3500000 and d > 5:
    print("APROBADO")

elif ("f == R") and ("e == C") and c < 2:
    print("APROBADO")

else:
    print("RECHAZADO")

