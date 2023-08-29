#Aprobación de créditos
ingreso = int(input("Ingrese su monto en pesos:"))
añonacimiento = int(input("Ingrese su año de nacimiento:"))
numerohijos = int(input("Ingrese cantidad de hijos:"))
añosenbanco = int(input("Ingrese años de pertenencia al banco]:"))
estado = str(input("Ingrese si es Soltero (S) o casado (C):"))
campociudad = str(input("Ingrese si vive en campo (R) o ciudad (U):"))

Añoactual = 2022
Edad = Añoactual - añonacimiento

if añosenbanco > 10 and numerohijos >= 2:
    print("APROBADO")

if str(estado) == "C" and numerohijos > 3 and Edad > 45 and Edad < 55:
    print("APROBADO")

if ingreso > 2500000 and str(estado) == "S" and str(campociudad) == "U":
    print("APROBADO")

if ingreso > 3500000 and añosenbanco > 5:
    print("APROBADO")

if str(campociudad) == "R" and str(estado) == "C" and numerohijos < 2:
    print("APROBADO")