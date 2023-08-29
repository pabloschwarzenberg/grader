#Aprobación de créditos
ingreso = int(input("Ingreso (en pesos): "))
año_nacimiento = int(input("Año de nacimiento: "))
numero_hijos = int(input("Número de hijos: "))
años_pertenencia = int(input("Años de pertenencia al banco: "))
estado_civil = input(str("Estado civil (""S"": soltero, ""C"":, casado ): "))
tipo_zona = input(str("Si vive en campo o cuidad (""U"": urbano, ""R"": rural): "))

mensaje = "RECHAZADO"

if años_pertenencia > 10 and numero_hijos >= 2:
    mensaje = "APROBADO"
elif estado_civil.upper() == "C" and numero_hijos > 3 and año_nacimiento > 1978 and año_nacimiento < 1988:
    mensaje = "APROBADO"
elif ingreso > 2500000 and estado_civil.upper() == "S" and tipo_zona.upper() == "U":
    mensaje = "APROBADO"
elif ingreso > 3500000 and años_pertenencia > 5:
    mensaje = "APROBADO"
elif tipo_zona.upper() == "R" and estado_civil.upper() == "C" and numero_hijos < 2:
    mensaje = "APROBADO"

print(mensaje)