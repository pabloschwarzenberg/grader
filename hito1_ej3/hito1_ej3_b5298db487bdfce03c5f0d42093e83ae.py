#Aprobación de créditos
Ingreso = int(input("Ingrese su Ingreso: "))
Año = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese su número de hijos: "))
Banco = int(input("Ingrese sus años en el banco: "))
Estado = input("Ingrese su Estado Civil 'S', soltero y 'C' Casado: ")
locacion = input("Ingrese si vive en campo 'R' o ciudad 'U': ")
edad = 2020 - Año


if Banco > 10 and Hijos >= 2:
    print("APROBADO")

if Estado == "C" and Hijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
if Ingreso > 2500000 and Estado == "S" and locacion == "U":
    print("APROBADO")
if Ingreso > 3500000 and Banco > 5:
    print("APROBADO")
if locacion == "R" and Estado == "C" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      