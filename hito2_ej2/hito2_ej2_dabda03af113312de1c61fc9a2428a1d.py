def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia_ingresada = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia_genoma(secuencia_ingresada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
