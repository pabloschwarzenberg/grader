sueldo = int(input("Indicar Sueldo Liquido en Pesos:   "))
añodenacimiento = int(input("Indicar año de nacimiento:  "))
hijos = int(input("Indicar cantidad de hijos:  "))
antiguedad = int(input("Indicar años de pertenencia al banco:  "))
estadocivil = str(input("Indicar estado civil s= Soltero, c= Casado:   "))
ubicacion = str(input("Indicar si vive en campo o ciudad; u = urbano; r= rural:  "))

c = str("C")
s = str("S")

u = str("U")
r = str("R")

edad = (2021 - añodenacimiento)

# print  (c)
# print(estadocivil)
if antiguedad > 10 and hijos >= 2:
    print("APROBADO")

elif antiguedad < 10 and hijos < 2:
    print("RECHAZADO")


elif estadocivil == c and hijos > 3 and edad > 45 and edad < 55:
    print("APROBADO")

elif estadocivil == s and hijos < 3 and edad < 45 and edad > 55:
    print("RECHAZADO")

elif sueldo > 2500000 and estadocivil == s and ubicacion == u:
    print("APROBADO")


elif sueldo > 3500000 and antiguedad > 5:
    print("APROBADO")

elif sueldo < 3500000 and antiguedad < 5:
    print("RECHAZADO")

elif ubicacion == r and estadocivil == c and hijos < 2:
    print("APROBADO")

elif ubicacion == u and estadocivil == s and hijos >= 2:
    print("RECHAZADO")

elif sueldo < 2500000 and estadocivil == c and ubicacion == r:
    print("RECHAZADO")
