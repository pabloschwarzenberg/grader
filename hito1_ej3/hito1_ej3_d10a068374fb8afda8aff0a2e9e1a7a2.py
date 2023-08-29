ingresos = int(input("Escriba sus ingresos en pesos: "))
agno_nacimiento = int(input("Ingrese su año de nacimiento: "))
cantidad_hijos = int(input("cantidad de hijos:"))
tiempo_banco = int(input("Ingrese los años en el banco: "))
estado_civil = input("S si es soltero; y C si esta casado: ")
campo_ciudad = input("Ingrese U si vive en ambiente urbano o R si vive en un ambiente rural: ")

if tiempo_banco >= 10 and cantidad_hijos >= 2:
    print("APROBADO")
elif estado_civil.upper() == "C" and cantidad_hijos > 3 and agno_nacimiento >= 45 or agno_nacimiento <= 55:
    print("APROBADO")
elif ingresos < 2500000 and estado_civil.upper() == "S" and campo_ciudad.upper() == "U":
    print("APROBADO")
elif ingresos > 3500000 and tiempo_banco > 5:
    print("APROBADO")
elif campo_ciudad.upper() == "R" and estado_civil.upper() == "C" and cantidad_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")