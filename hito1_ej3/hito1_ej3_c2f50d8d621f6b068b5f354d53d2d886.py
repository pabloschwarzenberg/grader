#Aprobación de crédito
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
#Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.


ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
vive_en = input("Ingrese si vive en campo o ciudad (U para urbano, R para rural): ")

if anos_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vive_en == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    print("APROBADO")
elif vive_en == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")