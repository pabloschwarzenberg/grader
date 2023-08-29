def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene solo A, C, T, G
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      