ingreso = int(input("Ingreso (en pesos): "))
año = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
años_banco = int(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil (\"S\": soltero, \"C\", casado): ")
zona = input("Si vive en campo o cuidad ("U": urbano, "R": rural): ")

edad = 2018 - año
aprobado = False

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(años_banco > 10 and hijos >= 2):
    aprobado = True

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if(estado_civil == "C" and hijos >= 3 and edad >= 45 and edad <= 55):
    aprobado = True
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
if(ingreso > 2500000 and estado_civil == "S" and zona == "U"):
    aprobado = True
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if(ingreso > 3500000 and años_banco >= 5):
    aprobado = True
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if(zona == "R" and estado_civil == "C" and hijos < 2):
    aprobado = True

if(aprobado == True):
    print("APROBADO")
else:
    print("RECHAZADO")      