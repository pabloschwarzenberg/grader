#Aprobación de créditos
P = int(input("Ingrese el ingreso en pesos: "))
A = int(input("Ingrese su año de nacimiento: "))
N = int(input("Ingrese cuantos hijos tiene: "))
B = int(input("Ingrese la cantidad de años perteneciente al banco: "))
E = str(input("Ingrese si esta soltero (S) o casado(C): "))
C = str(input("Ingrese si vive en campo(R) o ciudad(U): "))
edad = 2020 - A
if (B>= 10) and (N >= 2):
    print("APROBADO")
elif (E =="C") and (N>=3) and (45<=edad<=55):
    print("APROBADO")
elif (P>=2500000) and (E == "S") and (C == "U"):
    print("APROBADO")
elif (P>=350000) and (B>=5):
    print("APROBADO")
elif (C == "R") and (E == "C" ) and (N<2):
    print("APROBADO")
else:
    print("RECHAZADO")     