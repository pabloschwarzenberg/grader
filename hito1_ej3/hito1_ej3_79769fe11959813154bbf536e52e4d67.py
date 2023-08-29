#Aprobación de créditos
      #Banco
z = int(input("ingrese su monto en pesos:"))
x =int(input("ingrese su año de nacimiento:"))
c =int(input("ingrese su numero de hijos:"))
v = int(input("ingrese sus años de pertenencia en el banco:"))
b = str(input("ingrese su estado civil si es soltero (S), si es casado (C):"))
n = str(input("ingrese donde reside si vive en campo (R), si es ciudad (U):"))
año_actual = 2021
Edad = año_actual - x

if v > 10 and c >=2:
    print("APROBADO")

if str(b) == "C" and c > 3 and Edad > 45 and Edad < 55:
    print("APROBADO")

if z > 2500000 and str(b) == "S" and str(n) == "U":
    print("APROBADO")

if z > 3500000 and v > 5:
    print("APROBADO")

if str(n) == "R" and str(b) == "C" and c < 2:
    print("APROBADO")

else:
    print("RECHAZADO")

