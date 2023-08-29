#Aprobación de créditos
ingresos = int(input("Ingrese sus ingresos: "))
nacimiento = int(input("Ingrese su anio de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
ancliente = int(input("Cantidad de anios de clientes: "))
escivil = input("Estado civil, 'S' para soltero, 'C' para casado: ")
luvivienda = input("Lugar de vivienda, 'R' para Rural, 'U' para Urbano: ")

an = 2022 - nacimiento

if ancliente > 10 and hijos > 1:
    print("APROBADO")
elif escivil == "C" and hijos > 3 and 44 < an < 55:
    print("APROBADO")
elif ingresos > 2500000 and escivil == "S" and luvivienda == "U":
    print("APROBADO")
elif luvivienda == "R" and escivil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")