#Aprobación de créditos

from os import system
system ("cls")

Ingreso = int(input("ingreso"))
#(Pesos)
Ano_de_nacimiento = int(input("año"))
edad = Ano_de_nacimiento - 2023
Numero_de_hijos = int(input("hijos"))
Anos_de_pertenencia_al_banco = int(input("Año banco"))
Estado_civil = str(input("Estado civil (S/C): "))
#("S": soltero, "C", casado)
vive_en = str(input("vive (U/R): "))
#("U": urbano, "R": rural)

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if Anos_de_pertenencia_al_banco > 10 and Numero_de_hijos >= 2:
    print("APROBADO")

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif Estado_civil == "C" and Numero_de_hijos > 3 and 45 < edad < 55:
    print("APROBADO")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif Ingreso > 2500000 and Estado_civil == "S" and vive_en == "U":
    print("APROBADO")

#Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif Ingreso > 3500000 and Anos_de_pertenencia_al_banco > 5:
    print("APROBADO")

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif vive_en == "R" and Estado_civil == "C" and Numero_de_hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")