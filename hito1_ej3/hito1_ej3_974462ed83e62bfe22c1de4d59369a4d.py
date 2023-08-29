# i = ingreso
# a = año de nacimiento
# h = número de hijos
# b = número de años de pertenencia al banco
# e = estado civil = (S: soltero / C : casado)
# c = campo o ciudad = (U : urbano / R: rural(




i = int(input("Ingrese el total de sus ingresos: "))
a = int(input("Ingrese su año de nacimiento: "))
h = int(input("Indique el número de hijos que usted tiene: "))
b = int(input("Ingrese el número de años que usted lleva siendo cliente del banco: "))
e = str(input("Indique su estado civil: "))
c = str(input("Indique si vive en un entorno Rural o Urbano: "))
periodo = 2021



#condiciones
if  (i >= 2500000) and (e == "S") and (c == "U"):
    print("APROBADO")

elif (i >= 3500000) and (b >= 5):
    print("APROBADO")

elif (e == "C") and (h > 3) and (a - periodo >= 45 <= 55):
    print("APROBADO")

elif (b > 10) and (h >= 2):
    print("APROBADO")

elif (e == "C") and (h < 2) and (c == "R"):
    print("APROBADO")
else:
    print("Lo lamentamos, su crédito fue rechazado.")