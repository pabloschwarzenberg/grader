#Aprobación de créditos
ingreso = int(input("¿Cuál es su ingreso mensual? "))
anio = int(input("¿Cuál es su año de nacimiento? "))
hijos = int(input("¿Cuántos hijos tiene? "))
pertenencia = int(input("¿Cuántos años ha pertenecido al banco? "))
estado = input("¿Cúal es su estado civil? ((S) soltero , (C) casado ")
vivir = input("¿Dónde vive usted? ((R) campo , (U) ciudad) ")
edad = 2016-anio

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado == "C" and hijos > 3 and 45 < edad < 55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vivir == "U":
    print("APROBRADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivir == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")