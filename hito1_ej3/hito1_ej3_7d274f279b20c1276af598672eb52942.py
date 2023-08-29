print("Aprobación de Créditos")

ingreso = int(input("Ingresos (clp):"))
nacimiento = int(input("Año de nacimiento:"))
hijos = int(input("Numero de hijos:"))
a_servicio = int(input("Años de pertenencia al banco:"))
estado = str(input("Estado civil (S: soltero, C, casado):"))
vive = input("Si vive en campo o cuidad (U: urbano, R: rural):")

edad = 2023-nacimiento

condiciones = """Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
Si el cliente vive en el campo, es casado y tiene menos de dos hijos."""

if a_servicio > 10 and hijos >= 2:
    print("APROBADO")
elif estado == "C" and hijos > 3 and 45<=edad<=55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and a_servicio > 5:
    print("APROBADO")
elif vive == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      