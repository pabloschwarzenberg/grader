def validar_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    nucleotidos_validos = {'A', 'C', 'T', 'G'}  # Definir los nucleótidos válidos

    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False

    return True


# Obtener la secuencia del usuario
secuencia_input = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia del genoma
if validar_genoma(secuencia_input):
    print("Secuencia correcta. Representa un genoma válido.")
else:
    print("Secuencia incorrecta. No representa un genoma válido.")
