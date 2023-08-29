def evaluar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    # Verificar ingreso mínimo
    ingreso_minimo = 30000  # Monto mínimo requerido en pesos
    if ingreso < ingreso_minimo:
        return "Rechazado: ingreso insuficiente"

    # Verificar edad
    edad_minima = 18  # Edad mínima requerida
    ano_actual = 2023  # Asumimos que estamos en el año actual
    edad = ano_actual - ano_nacimiento
    if edad < edad_minima:
        return "Rechazado: edad mínima no alcanzada"

    # Verificar número de hijos
    hijos_maximos = 4  # Número máximo de hijos permitidos
    if num_hijos > hijos_maximos:
        return "Rechazado: excede el número máximo de hijos permitidos"

    # Verificar años de pertenencia al banco
    anos_pertenencia_minimos = 2  # Mínimo de años de pertenencia requeridos
    if anos_pertenencia < anos_pertenencia_minimos:
        return "Rechazado: años de pertenencia al banco insuficientes"

    # Verificar estado civil
    if estado_civil not in ["S", "C"]:
        return "Rechazado: estado civil inválido"

    # Verificar ubicación
    if ubicacion not in ["U", "R"]:
        return "Rechazado: ubicación inválida"

    # Si se pasan todas las verificaciones, se aprueba el crédito
    return "Aprobado"

# Ejemplo de uso
ingreso = 45000
ano_nacimiento = 1990
num_hijos = 2
anos_pertenencia = 3
estado_civil = "C"
ubicacion = "U"

resultado = evaluar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)
print(resultado)
