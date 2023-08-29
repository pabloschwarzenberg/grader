#Aprobación de créditos
 ingresos = int(input("Ingrese sus ingreso: "))
anio_nacimiento = int(input("Ingrese su fecha de nacimiento: "))
numero_hijos = int(input("Ingrese cuantos hijos tiene: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil de S para soltero y de C para casado: ")
ubicacion = input("Ingrese su ubicación eliga entre U de urbano y R de rural: ")

aprobado = False

if anios_banco > 10 and numero_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and numero_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    aprobado = True
elif ingresos > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingresos > 3500000 and anios_banco > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and numero_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")     