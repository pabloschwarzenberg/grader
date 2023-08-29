ingreso = int(input("ingrese su ingreso en pesos:"))
nacimiento = int(input("ingrese su año de nacimiento:"))
hijos = int(input("ingrese numero de hijos:"))
tiempo = int(input("ingrese hace cuantos años pertenece al banco:"))
estado = str(input("ingrese su estado civil, soltero (S) o casado (C):"))
vive = str(input("ingrese si vive en campo (R) o ciudad (U):"))
edad = 2021 - nacimiento

if tiempo > 10 and hijos >= 2:
    print("CREDITO APROBADO")
elif tiempo <= 10 or hijos < 2:
        print("CREDITO RECHAZADO")

if estado == "C" and hijos > 3 and edad >= 45 <= 55:
    print("CREDITO APROBADO")
elif estado == "S" or hijos > 3 or edad < 45 > 55:
        print("CREDITO RECHAZADO")

if ingreso > 250000 and estado == "S" and vive == "U":
    print("CREDITO APROBADO")
elif ingreso <= 250000 or estado == "C" or vive == "R":
        print("CREDITO RECHAZADO")

if ingreso > 350000 and tiempo > 5:
    print("CREDITO APROBADO")
elif ingreso <= 350000 or tiempo <= 5:
        print("CREDITO RECHAZADO")

if vive == "R" and estado == "C" and hijos < 2:
    print("CREDITO APROBADO")
elif vive == "U" or estado == "S" or hijos >=2:
        print("CREDITO RECHAZADO")