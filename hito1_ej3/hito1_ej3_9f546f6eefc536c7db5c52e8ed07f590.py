ingreso = float(input("Ingrese su ingreso mensual en pesos: "))
ano_de_nacimiento = int(input("Ingrese su ano de nacimiento: "))
numeros_de_hijos = int(input("Ingrese el numero de hijos que tiene: "))
anos_en_el_banco = int(input("Ingrese la cantidad de anos que lleva en el banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese su ubicacion (U: urbano, R: rural): ")

aprobado = False

if anos_en_el_banco > 10 and numeros_de_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and numeros_de_hijos > 3 and 45 <= (2023 - ano_de_nacimiento) <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingreso > 3500000 and anos_en_el_banco > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and numeros_de_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")