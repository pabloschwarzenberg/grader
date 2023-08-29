#Aprobación de créditos
ingreso           = int(input("Ingreso: "))
anio_nacimiento   = int(input("Año nacimiento: "))
nro_hijos         = int(input("Número de hijos: "))
anios_pertenencia = int(input("Años de pertenencia al banco: "))
estado_civil      = input("Estado civil(S: soltero, C: casado): ")
lugar             = input("Vive en campo o ciudad(U: urbano, R: rural): ")


edad = 2021 - anio_nacimiento
estado_civil = estado_civil.upper()
lugar = lugar.upper()

resultado = "RECHAZADO"

if anios_pertenencia >= 10 and nro_hijos >= 2:
    resultado = "APROBADO"

elif estado_civil == 'C' and nro_hijos > 3 \
    and edad >= 45 and edad <= 55:
    resultado = "APROBADO"

elif ingreso > 2500000 and estado_civil == 'S' and lugar == 'U':
    resultado = "APROBADO"

elif ingreso > 3500000 and anios_pertenencia > 5:
    resultado = "APROBADO"

elif lugar == 'R' and estado_civil == 'C' and nro_hijos < 2:
    resultado = "APROBADO"

print(resultado)
