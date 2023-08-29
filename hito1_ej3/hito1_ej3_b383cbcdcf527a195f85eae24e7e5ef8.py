# Un Banco desea implementar una política de atención automatizada de créditos de consumo,
# y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

# Ingreso (en pesos)
# Año de nacimiento
# Número de hijos
# Años de pertenencia al banco
# Estado civil ("S": soltero, "C", casado)
# Si vive en campo o cuidad ("U": urbano, "R": rural)

# El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

# Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
# Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
# Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
# Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
# Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.


# Aprobación de créditos
ingreso = int(input("Ingreso: "))
año_nacimiento = int(input("Ingresa año de nacimiento: "))
edad = año_nacimiento - 2023
numero_de_hijos = int(input("Ingresa años de pertenencia al banco: "))
año_en_banco = int(input("Ingresa años de pertenencia al banco: "))
estado_civil = str(input("Ingresa estado civil:\n"
                   "Soltero = S, Casado = C\n"))
campo_o_ciudad = str(input("Vivienda: Campo o Ciudad:\n"
                           "Urbano = U, Rural = R\n"))

if año_en_banco >= 10 and numero_de_hijos >= 2:
    resultado = "APROBADO"
elif estado_civil == "C" and numero_de_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
    resultado = "APROBADO"
elif ingreso >= 2500000 and estado_civil == "S" and campo_o_ciudad == "U":
    resultado = "APROBADO"
elif ingreso >= 3500000 and año_en_banco >= 5:
    resultado = "APROBADO"
elif campo_o_ciudad == "R" and estado_civil == "C" and numero_de_hijos <= 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

print(resultado)
