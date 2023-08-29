#Aprobación de créditos
ingreso = int(input("Ingrese ingresos(en pesos): "))
nacimiento = int(input("Ingrese año de nacimiento: "))
banco = int(input("Ingrese años de pertenencia en el banco: "))
hijos = int(input("Ingrese numero de hijos: "))
estado = input("Ingrese estado civil: ")
vive = input("Ingrese donde vive: ")

if banco > 10 and hijos >= 2:
    resultado = "APROBADO"
elif estado == "C" and hijos > 3 and 1966 < nacimiento < 1976:
    resultado = "APROBADO"
elif ingreso > 2500000 and estado == "S" and vive == "R":
    resultado = "APROBADO"
elif ingreso > 3500000 and banco > 5:
    resultado = "APROBADO"
elif vive == "U" and estado == "C" and hijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"


print(resultado)      