def evaluar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return "Crédito aprobado"

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return "Crédito aprobado"

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "Crédito aprobado"

    if ingreso > 3500000 and anios_pertenencia > 5:
        return "Crédito aprobado"

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "Crédito aprobado"

    return "Crédito no aprobado"

# Datos de ejemplo 1
ingreso1 = 250000
anio_nacimiento1 = 1970
num_hijos1 = 4
anios_pertenencia1 = 11
estado_civil1 = "C"
ubicacion1 = "R"

resultado1 = evaluar_credito(ingreso1, anio_nacimiento1, num_hijos1, anios_pertenencia1, estado_civil1, ubicacion1)
print("Datos de ejemplo 1:")
print("Ingreso:", ingreso1)
print("Año de nacimiento:", anio_nacimiento1)
print("Número de hijos:", num_hijos1)
print("Años de pertenencia al banco:", anios_pertenencia1)
print("Estado civil:", estado_civil1)
print("Ubicación:", ubicacion1)
print("Resultado:", resultado1)

# Datos de ejemplo 2
ingreso2 = 350000
anio_nacimiento2 = 1970
num_hijos2 = 4
anios_pertenencia2 = 11
estado_civil2 = "S"
ubicacion2 = "U"

resultado2 = evaluar_credito(ingreso2, anio_nacimiento2, num_hijos2, anios_pertenencia2, estado_civil2, ubicacion2)
print("\nDatos de ejemplo 2:")
print("Ingreso:", ingreso2)
print("Año de nacimiento:", anio_nacimiento2)
print("Número de hijos:", num_hijos2)
print("Años de pertenencia al banco:", anios_pertenencia2)
print("Estado civil:", estado_civil2)
print("Ubicación:", ubicacion2)
print("Resultado:", resultado2)

# Datos de ejemplo 3
ingreso3 = 450000
anio_nacimiento3 = 1970
num_hijos3 = 4
anios_pertenencia3 = 11
estado_civil3 = "S"
ubicacion3 = "U"

resultado3 = evaluar_credito(ingreso3, anio_nacimiento3, num_hijos3, anios_pertenencia3, estado_civil3, ubicacion3)
print("\nDatos de ejemplo 3:")
print("Ingreso:", ingreso3)
print("Año de nacimiento:", anio_nacimiento3)
print("Número de hijos:", num_hijos3)
print("Años de pertenencia al banco:", anios_pertenencia3)
print("Estado civil:", estado_civil3)
print("Ubicación:", ubicacion3)
print("Resultado:", resultado3)

# Datos de ejemplo 4
ingreso4 = 450000
anio_nacimiento4 = 1970
num_hijos4 = 1
anios_pertenencia4 = 11
estado_civil4 = "C"
ubicacion4 = "R"

resultado4 = evaluar_credito(ingreso4, anio_nacimiento4, num_hijos4, anios_pertenencia4, estado_civil4, ubicacion4)
print("\nDatos de ejemplo 4:")
print("Ingreso:", ingreso4)
print("Año de nacimiento:", anio_nacimiento4)
print("Número de hijos:", num_hijos4)
print("Años de pertenencia al banco:", anios_pertenencia4)
print("Estado civil:", estado_civil4)
print("Ubicación:", ubicacion4)
print("Resultado:", resultado4)
