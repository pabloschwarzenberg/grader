def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    for base in secuencia:
        if base not in ['A', 'C', 'T', 'G']:
            return False
    return True

# Obtener la secuencia del usuario
secuencia_genoma = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      