#Aprobación de créditos
#Entrada.
print("Bienvenido a la atención de créditos de consumo.")
Ingreso = int(input("Ingrese su cantidad de ingresos en pesos: "))
Nacim = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese su número de hijos: "))
Perte = int(input("Ingrese sus años de pertenencia en el banco: "))
Estado = str(input("Ingrese su estado civil: "))
Residenc = str(input("Ingrese si vive en campo o ciudad: "))
#Procesamiento y salida.
if Perte > 10 and Hijos >= 2:
    print("APROBADO.")
else:
    print("RECHAZADO.")

if Estado == "C" and Hijos > 3 and 1977 <= Nacim >= 1987:
    print("APROBADO.")
else:
    print("RECHAZADO.")

if Ingreso > 2500000 and Estado == "S" and Residenc == "U":
    print("APROBADO.")
else:
    print("RECHAZADO.")

if Ingreso > 3500000 and Perte > 5:
    print("APROBADO.")
else:
    print("RECHAZADO.")

if Residenc == "R" and Estado == "C" and Hijos < 2:
    print("APROBADO.")
else:
    print("RECHAZADO.")
          