#Aprobación de créditos
print("Solicitud de Créditos de Consumo\n")
ingreso = int(input("Ingrese el monto de sus ingresos: "))
nacimiento = int(input("Ingrese el año de su nacimiento: " ))
hijos = int(input("Ingrese la cantidad de hijos: "))
antiguedad = int(input("Ingrese la cantidad de años de antigüedad en el banco: "))
estado = input("Ingrese su estado civil (S: soltero, C, casad@): ")
estado = estado.upper()
localidad = input("Donde vive (U: urbano, R: rural): ")
localidad = localidad.upper()

if antiguedad > 10 and hijos >= 2:
    resultado = "APROBADO"
elif estado == "C" and hijos > 3 and nacimiento >= 1967 and nacimiento <= 1977:
    resultado = "APROBADO"
elif ingreso > 2500000 and estado == "S" and localidad == "U":
    resultado = "APROBADO"
elif ingreso > 3500000 and antiguedad > 5:
    resultado = "APROBADO"
elif localidad == "R" and estado == "C" and hijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"
print("Su solicitud a sido", resultado)
print(resultado)      